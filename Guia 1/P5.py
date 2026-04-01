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