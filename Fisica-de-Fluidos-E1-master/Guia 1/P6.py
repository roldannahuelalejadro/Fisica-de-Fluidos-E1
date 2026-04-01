import numpy as np
import matplotlib.pyplot as plt

# malla espacial
x = np.linspace(-5,5,200)
y = np.linspace(-5,5,200)
print(x)
X,Y = np.meshgrid(x,y)

# punto inicial de la partícula
x0, y0 = 1, 1

# ===============================
# (i) Corriente uniforme
# ===============================

U = 5

u = U*np.ones_like(X)
v = np.zeros_like(X)

print(len(u), len(v), len(x), len(y))

plt.figure()
plt.streamplot(X,Y,u,v)

# trayectoria
t = np.linspace(0,5,200)
x_traj = x0 + U*t
y_traj = y0*np.ones_like(t)



plt.title("Corriente uniforme")
plt.legend()
plt.show()


# ===============================
# (ii) Fuente lineal
# ===============================

Q = 5
r = np.sqrt(X**2 + Y**2)

u = Q/(2*np.pi) * X/(r**2 + 1e-8)
v = Q/(2*np.pi) * Y/(r**2 + 1e-8)

plt.figure()
plt.streamplot(X,Y,u,v)

# trayectoria radial
t = np.linspace(0,5,200)
r0 = np.sqrt(x0**2 + y0**2)
theta0 = np.arctan2(y0,x0)

r_traj = np.sqrt(r0**2 + (Q/np.pi)*t)

x_traj = r_traj*np.cos(theta0)
y_traj = r_traj*np.sin(theta0)



plt.title("Fuente lineal")
plt.legend()
plt.show()


# ===============================
# (iii) Torbellino
# ===============================

Gamma = 5

u = -Gamma/(2*np.pi) * Y/(X**2 + Y**2 + 1e-8)
v =  Gamma/(2*np.pi) * X/(X**2 + Y**2 + 1e-8)

plt.figure()
plt.streamplot(X,Y,u,v)

# trayectoria circular
t = np.linspace(0,10,400)

r0 = np.sqrt(x0**2 + y0**2)
theta0 = np.arctan2(y0,x0)

theta = theta0 + Gamma/(2*np.pi*r0**2)*t

x_traj = r0*np.cos(theta)
y_traj = r0*np.sin(theta)



plt.title("Torbellino")
plt.legend()
plt.show()