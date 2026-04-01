import numpy as np
import matplotlib.pyplot as plt

# =====================
# Parámetros del problema
# =====================

T0 = 300        # temperatura base
alpha = 20      # amplitud
L = 10          # longitud característica
tau = 5         # periodo temporal
U = 50           # velocidad de la partícula

# dominio espacial
x = np.linspace(0, 50, 500)

# tiempos cercanos
t0 = 1
times = np.linspace(t0, 10*t0, 100)

# =====================
# campo de temperatura
# =====================

def T(x, t):
    return T0 - alpha * np.exp(-x/L) * np.sin(2*np.pi*t/tau)

# =====================
# gráfico
# =====================

plt.figure()

for t in times:
    plt.plot(x, T(x, t), label=f"t = {t:.2f}")

plt.xlabel("x")
plt.ylabel("T(x,t)")
plt.title("Campo de temperatura en instantes cercanos")
# plt.legend()

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# =====================
# Parámetros
# =====================

T0 = 300
alpha = 20
L = 10
tau = 5

# dominios
x = np.linspace(0, 50, 200)
t = np.linspace(0, 10, 200)

# grilla 2D
X, T = np.meshgrid(x, t)

# campo de temperatura
Temp = T0 - alpha * np.exp(-X/L) * np.sin(2*np.pi*T/tau)

# =====================
# gráfico 3D
# =====================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, T, Temp)

ax.set_xlabel("x")
ax.set_ylabel("t")
ax.set_zlabel("T(x,t)")
ax.set_title("Superficie de temperatura T(x,t)")

plt.show()
