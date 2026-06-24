import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Sistema 1
A = np.array([
    [4, -1],
    [2,  1]
])

def sistema_1(t, z):
    x, y = z
    dx = 4*x - y
    dy = 2*x + y
    return [dx, dy]

# Grilla para el campo vectorial
x = np.linspace(-3, 3, 25)
y = np.linspace(-3, 3, 25)
X, Y = np.meshgrid(x, y)

U = 4*X - Y
V = 2*X + Y

# Normalización para que las flechas sean más legibles
N = np.sqrt(U**2 + V**2)
U_norm = U / (N + 1e-8)
V_norm = V / (N + 1e-8)

plt.figure(figsize=(7, 7))

# Campo vectorial
plt.quiver(X, Y, U_norm, V_norm, alpha=0.7)

# Streamplot
plt.streamplot(X, Y, U, V, density=1.2)

# Punto fijo
plt.scatter([0], [0], color="black", s=80, label="Punto fijo")

# Direcciones propias
xx = np.linspace(-3, 3, 200)
plt.plot(xx, xx, "--", label=r"$y=x$")
plt.plot(xx, 2*xx, "--", label=r"$y=2x$")

# Trayectorias numéricas desde varias condiciones iniciales
condiciones_iniciales = [
    [0.2, 0.1],
    [-0.2, -0.1],
    [0.5, 1.0],
    [-0.5, -1.0],
    [1.0, 0.2],
    [-1.0, -0.2],
    [0.2, 1.0],
    [-0.2, -1.0],
]

for z0 in condiciones_iniciales:
    sol = solve_ivp(sistema_1, [0, 1.2], z0, t_eval=np.linspace(0, 1.2, 300))
    plt.plot(sol.y[0], sol.y[1], linewidth=2)

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.title(r"Sistema 1: nodo inestable")
plt.legend()
plt.grid(False)
plt.show()