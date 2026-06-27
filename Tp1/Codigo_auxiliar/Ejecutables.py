import numpy as np
import matplotlib.pyplot as plt

# malla espacial
x = np.linspace(-5,5,200)
y = np.linspace(-5,5,200)
X,Y = np.meshgrid(x,y)


x0, y0 = 1, 1

U = 5
U_prima = 3
tau = 0.5

# Ejercicio 1 (i):
t = np.linspace(0,0.5,10)
t_fijo = 0.6
for t_i in t:
    u = U * np.ones_like(X)
    v = U_prima * np.cos(2*np.pi * t_i /tau) * np.ones_like(X)
    print(u.shape)
    print(v.shape)

    #plt.figure()
    #plt.streamplot(X,Y,u,v)

    # trayectoria

    x_traj = U*t+x0
    y_traj = (tau/2*np.pi)*U_prima * np.sin(2*np.pi * t / tau) + y0

    #plt.legend()
    #plt.show()
    
#%% Ejercicio 1 (ii):

import numpy as np
import matplotlib.pyplot as plt

# malla espacial
x = np.linspace(-5,5,200)
y = np.linspace(-5,5,200)
X,Y = np.meshgrid(x,y)

t = np.linspace(0,0.5,10)
t_fijo = 0.6

alpha = 0.1
beta = 3
c = 10

for t_i in t:
    u = (alpha /(1+beta * t_i)) * X
    print(u.shape)
    print(v.shape)

    plt.figure()
    plt.streamplot(X,Y,u,v)

    # trayectoria

    #x_traj = U*t+x0
    #y_traj = (tau/2*np.pi)*U_prima * np.sin(2*np.pi * t / tau) + y0


    plt.legend()
    plt.show()





#====================================================================0
#def esquema(X, u, t, dt):
#  """
#  Calcula X(t+dt) a partir de X(t) y el campo de velocidades,
#  usando el esquema de Euler (MALO)
#
#  Parámetros:
#    X : Solución a tiempo t (X(t)) cómo arreglo de dimensión d
#    u : Campo de velocidades cómo función de (x,t)
#    t : Tiempo donde se conoce t
#    dt: Paso temporal
#  """
#  return X + u(X,t)*dt
#
#u = lambda X, t: np.array([np.cos(X[1]), np.cos(X[0])])
#N = 1000
#dt = 1e-2
#p0s = np.array([[-1, 0], [1, 0], [-0.4, 0], [0.4, 0]])
#
#fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(12,5), constrained_layout=True,
#                               sharex=True, sharey=True)
#for i in range(4):
#  _, Xs = trayectoria(p0s[i], u, N, dt)
#  ax1.plot(Xs[0,0], Xs[0,1], "ko")
#  ax1.plot(Xs[:,0], Xs[:,1], "b-")
#
#N = 10000
#ds = 1e-3
#for i in range(4):
#  _, ls = linea_de_corriente(p0s[i], u, 0, N, ds)
#  ax2.plot(ls[0,0], ls[0,1], "ko")
#  ax2.plot(ls[:,0], ls[:,1], "b-")
#
#ax1.set_xlim(-4,4)
#ax1.set_ylim(-4,4)
#ax1.set_xlabel('$kx$', fontsize=14)
#ax1.set_ylabel('$ky$', fontsize=14)
#ax1.set_title(f'Trayectorias | d$t={dt}$', fontsize=16)
#ax2.set_xlabel('$kx$', fontsize=14)
#ax2.set_ylabel('$ky$', fontsize=14)
#ax2.set_title(f'Líneas de