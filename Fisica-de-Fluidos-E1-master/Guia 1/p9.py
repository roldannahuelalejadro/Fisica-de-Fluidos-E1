import numpy as np
import matplotlib.pyplot as plt

# ===================== PARÁMETROS =====================
Omega = 1.0
a = 1.0

# ===================== GRILLA =====================
L = 3.0 * a
N = 300

x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)

# Evitar división por cero en r = 0
R_safe = np.where(R == 0, 1e-12, R)

# ===================== VELOCIDAD AZIMUTAL =====================
vtheta = np.where(
    R < a,
    Omega * R,
    Omega * a**2 / R_safe
)

# Componentes cartesianas
Vx = -vtheta * Y / R_safe
Vy =  vtheta * X / R_safe

# En el origen la velocidad debe ser cero
Vx[R == 0] = 0.0
Vy[R == 0] = 0.0

# ===================== GRÁFICO =====================
fig, ax = plt.subplots(figsize=(7, 7))

speed = np.sqrt(Vx**2 + Vy**2)

stream = ax.streamplot(
    X, Y,
    Vx, Vy,
    density=1.8,
    linewidth=1.0,
    arrowsize=1.2
)

# Círculo que separa núcleo y exterior
circle = plt.Circle(
    (0, 0),
    a,
    fill=False,
    linestyle="--",
    linewidth=2,
    label=r"$r=a$"
)

ax.add_patch(circle)

ax.set_aspect("equal")
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_title(r"Líneas de campo del vórtice de Rankine")

ax.legend()
plt.show()