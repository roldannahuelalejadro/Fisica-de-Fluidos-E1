import numpy as np
import matplotlib.pyplot as plt


def rk4(f, z0, t):
    """
    Integra z' = f(t,z) usando Runge-Kutta de orden 4.
    """
    z = np.zeros((len(t), len(z0)), dtype=float)
    z[0] = np.array(z0, dtype=float)

    for n in range(len(t)-1):
        h = t[n+1] - t[n]
        tn = t[n]
        zn = z[n]

        k1 = np.array(f(tn, zn))
        k2 = np.array(f(tn + h/2, zn + h*k1/2))
        k3 = np.array(f(tn + h/2, zn + h*k2/2))
        k4 = np.array(f(tn + h, zn + h*k3))

        z[n+1] = zn + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    return z


def plot_phase_portrait(
    f,
    xlim,
    ylim,
    fixed_points=None,
    nullcline_curves=None,
    trajectories=None,
    title="Diagrama de fases",
    xlabel=r"$x$",
    ylabel=r"$y$",
    density=1.2,
    grid_points=31,
    tmax=6,
    both_time_directions=True
):
    x = np.linspace(xlim[0], xlim[1], grid_points)
    y = np.linspace(ylim[0], ylim[1], grid_points)
    X, Y = np.meshgrid(x, y)

    U = np.zeros_like(X)
    V = np.zeros_like(Y)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            dx, dy = f(0, [X[i, j], Y[i, j]])
            U[i, j] = dx
            V[i, j] = dy

    N = np.sqrt(U**2 + V**2)
    U_norm = U / (N + 1e-12)
    V_norm = V / (N + 1e-12)

    plt.figure(figsize=(8, 7))
    plt.quiver(X, Y, U_norm, V_norm, alpha=0.55)
    plt.streamplot(X, Y, U, V, density=density, linewidth=1)

    if nullcline_curves is not None:
        for curve in nullcline_curves:
            plt.plot(curve["x"], curve["y"], linewidth=2.5, label=curve.get("label", "nulclina"))

    if fixed_points is not None:
        for p in fixed_points:
            plt.scatter([p[0]], [p[1]], s=90, color="black", zorder=5)
            plt.text(p[0], p[1], f"  ({p[0]:.2g},{p[1]:.2g})", fontsize=10)

    if trajectories is not None:
        t_forward = np.linspace(0, tmax, 700)
        t_backward = np.linspace(0, -tmax, 700)
        for z0 in trajectories:
            sol_f = rk4(f, z0, t_forward)
            plt.plot(sol_f[:, 0], sol_f[:, 1], linewidth=2)
            if both_time_directions:
                sol_b = rk4(f, z0, t_backward)
                plt.plot(sol_b[:, 0], sol_b[:, 1], linewidth=2)

    plt.axhline(0, linewidth=0.8, color="black")
    plt.axvline(0, linewidth=0.8, color="black")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc="best")
    plt.grid(False)
    plt.show()



# Sistema 1: x' = x - x^3, y' = -y

def sistema_1(t, z):
    x, y = z
    return [x - x**3, -y]

fixed_points_1 = [(-1, 0), (0, 0), (1, 0)]

xx = np.linspace(-2.5, 2.5, 400)
yy = np.linspace(-2.5, 2.5, 400)

nullclines_1 = [
    {"x": -np.ones_like(yy), "y": yy, "label": r"$\dot{x}=0$: $x=-1$"},
    {"x": np.zeros_like(yy), "y": yy, "label": r"$\dot{x}=0$: $x=0$"},
    {"x": np.ones_like(yy), "y": yy, "label": r"$\dot{x}=0$: $x=1$"},
    {"x": xx, "y": np.zeros_like(xx), "label": r"$\dot{y}=0$: $y=0$"},
]

trajectories_1 = [
    [-2, 2], [-2, -2],
    [-0.5, 2], [-0.5, -2],
    [0.5, 2], [0.5, -2],
    [2, 2], [2, -2],
    [0, 1.5], [0, -1.5],
]

plot_phase_portrait(
    sistema_1,
    xlim=(-2.5, 2.5),
    ylim=(-2.5, 2.5),
    fixed_points=fixed_points_1,
    nullcline_curves=nullclines_1,
    trajectories=trajectories_1,
    title=r"Sistema 1: $\dot{x}=x-x^3$, $\dot{y}=-y$",
    tmax=6
)

# Sistema 2: x' = x - y, y' = x^2 - 4

def sistema_2(t, z):
    x, y = z
    return [x - y, x**2 - 4]

fixed_points_2 = [(-2, -2), (2, 2)]

xx = np.linspace(-4, 4, 400)
yy = np.linspace(-5, 5, 400)

nullclines_2 = [
    {"x": xx, "y": xx, "label": r"$\dot{x}=0$: $y=x$"},
    {"x": -2*np.ones_like(yy), "y": yy, "label": r"$\dot{y}=0$: $x=-2$"},
    {"x": 2*np.ones_like(yy), "y": yy, "label": r"$\dot{y}=0$: $x=2$"},
]

trajectories_2 = [
    [-3.5, -3.5], [-2.5, -2], [-1.5, -2],
    [1.5, 2.0], [2.2, 2.0], [2.0, 1.6], [2.0, 2.4],
    [0, 0], [0, 3], [0, -3],
    [3, 0], [-3, 0]
]

plot_phase_portrait(
    sistema_2,
    xlim=(-4, 4),
    ylim=(-5, 5),
    fixed_points=fixed_points_2,
    nullcline_curves=nullclines_2,
    trajectories=trajectories_2,
    title=r"Sistema 2: $\dot{x}=x-y$, $\dot{y}=x^2-4$",
    tmax=3.5
)

# Sistema 3: x' = x(2-x-y), y' = x-y

def sistema_3(t, z):
    x, y = z
    return [x*(2 - x - y), x - y]

fixed_points_3 = [(0, 0), (1, 1)]

xx = np.linspace(-1, 4, 400)
yy = np.linspace(-1, 4, 400)

nullclines_3 = [
    {"x": np.zeros_like(yy), "y": yy, "label": r"$\dot{x}=0$: $x=0$"},
    {"x": xx, "y": 2 - xx, "label": r"$\dot{x}=0$: $y=2-x$"},
    {"x": xx, "y": xx, "label": r"$\dot{y}=0$: $y=x$"},
]

trajectories_3 = [
    [0.2, 0.2], [0.5, 3], [3, 0.5], [2.5, 2.5],
    [1.5, 0.2], [0.2, 1.5], [3.5, 1],
    [-0.5, 0.5], [-0.5, 2],
    [0, 2], [0, -0.5]
]

plot_phase_portrait(
    sistema_3,
    xlim=(-1, 4),
    ylim=(-1, 4),
    fixed_points=fixed_points_3,
    nullcline_curves=nullclines_3,
    trajectories=trajectories_3,
    title=r"Sistema 3: $\dot{x}=x(2-x-y)$, $\dot{y}=x-y$",
    tmax=8
)


# Sistema 4: péndulo θ' = ω, ω' = -(g/l) sin(θ)

g = 9.81
l = 1.0
alpha = g/l

def pendulo(t, z):
    theta, omega = z
    return [omega, -alpha*np.sin(theta)]

theta_min = -2*np.pi
theta_max = 2*np.pi
omega_min = -4
omega_max = 4

theta_vals = np.linspace(theta_min, theta_max, 800)
omega_vals = np.linspace(omega_min, omega_max, 400)

fixed_points_pendulo = []
for n in range(-3, 4):
    th = n*np.pi
    if theta_min <= th <= theta_max:
        fixed_points_pendulo.append((th, 0))

nullclines_pendulo = [
    {"x": theta_vals, "y": np.zeros_like(theta_vals), "label": r"$\dot{\theta}=0$: $\omega=0$"}
]

for n in range(-2, 3):
    th = n*np.pi
    nullclines_pendulo.append({
        "x": th*np.ones_like(omega_vals),
        "y": omega_vals,
        "label": rf"$\dot{{\omega}}=0$: $\theta={n}\pi$"
    })

trajectories_pendulo = [
    [0.2, 0.0], [0.8, 0.0], [1.5, 0.0], [2.5, 0.0],
    [0.0, 2.0], [0.0, 3.5], [-0.8, 0.0], [-1.5, 0.0],
    [-2.5, 0.0], [np.pi + 0.1, 0.0], [-np.pi + 0.1, 0.0]
]

plot_phase_portrait(
    pendulo,
    xlim=(theta_min, theta_max),
    ylim=(omega_min, omega_max),
    fixed_points=fixed_points_pendulo,
    nullcline_curves=nullclines_pendulo,
    trajectories=trajectories_pendulo,
    title=r"Péndulo: $\dot{\theta}=\omega$, $\dot{\omega}=-(g/l)\sin\theta$",
    xlabel=r"$\theta$",
    ylabel=r"$\omega$",
    tmax=8,
    grid_points=35,
    density=1.5,
    both_time_directions=False
)

# Curvas de energía del péndulo
Theta, Omega = np.meshgrid(
    np.linspace(theta_min, theta_max, 500),
    np.linspace(omega_min, omega_max, 500)
)

E = 0.5*Omega**2 + alpha*(1 - np.cos(Theta))

plt.figure(figsize=(9, 6))
plt.contour(Theta, Omega, E, levels=25)
plt.axhline(0, color="black", linewidth=0.8)
for n in range(-2, 3):
    plt.axvline(n*np.pi, color="black", linewidth=0.5)

for p in fixed_points_pendulo:
    n_aprox = round(p[0]/np.pi)
    if n_aprox % 2 == 0:
        plt.scatter([p[0]], [p[1]], s=90, color="black", label="Centro" if p[0] == 0 else None)
    else:
        plt.scatter([p[0]], [p[1]], s=90, facecolors="white", edgecolors="black", linewidths=2, label="Silla" if abs(p[0] - np.pi) < 1e-8 else None)

plt.xlim(theta_min, theta_max)
plt.ylim(omega_min, omega_max)
plt.xlabel(r"$\theta$")
plt.ylabel(r"$\omega$")
plt.title(r"Péndulo: curvas de energía")
plt.legend()
plt.grid(False)
plt.show()
