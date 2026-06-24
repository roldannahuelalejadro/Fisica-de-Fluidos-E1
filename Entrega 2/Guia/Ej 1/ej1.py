import numpy as np
import matplotlib.pyplot as plt

def phase_line(ax, fixed_points, stability, intervals, xlim, title):
    """
    Dibuja un retrato de fase 1D.

    fixed_points: lista de puntos fijos
    stability: lista con "estable", "inestable" o "semestable"
    intervals: lista de tuplas (x_left, x_right, direction)
               direction = +1 para flecha derecha, -1 para flecha izquierda
    xlim: límites del eje x
    """
    ax.set_xlim(*xlim)
    ax.set_ylim(-1, 1)
    ax.axhline(0, color="black", linewidth=1.5)

    # Flechas en cada intervalo
    for left, right, direction in intervals:
        mid = (left + right) / 2
        length = 0.45 * (right - left)

        if direction > 0:
            start = mid - length/2
            dx = length
        else:
            start = mid + length/2
            dx = -length

        ax.annotate(
            "",
            xy=(start + dx, 0),
            xytext=(start, 0),
            arrowprops=dict(arrowstyle="->", linewidth=2)
        )

    # Puntos fijos
    for xstar, stab in zip(fixed_points, stability):
        if stab == "estable":
            marker = "o"
            facecolor = "black"
        elif stab == "inestable":
            marker = "o"
            facecolor = "white"
        else:
            marker = "o"
            facecolor = "gray"

        ax.scatter(
            [xstar], [0],
            s=120,
            marker=marker,
            facecolors=facecolor,
            edgecolors="black",
            linewidths=2,
            zorder=3
        )

        ax.text(
            xstar, -0.22,
            rf"${xstar:.2g}$" if abs(xstar) not in [np.pi/3, 5*np.pi/3] else "",
            ha="center",
            va="top",
            fontsize=10
        )

    ax.set_yticks([])
    ax.set_xlabel(r"$x$")
    ax.set_title(title)
    ax.spines[["left", "right", "top"]].set_visible(False)


fig, axes = plt.subplots(3, 1, figsize=(10, 7))

# 1) dx/dt = ax, caso a > 0
phase_line(
    axes[0],
    fixed_points=[0],
    stability=["inestable"],
    intervals=[(-3, 0, -1), (0, 3, +1)],
    xlim=(-3, 3),
    title=r"Retrato de fase: $\dot{x}=ax$, caso $a>0$"
)

# 2) dx/dt = x - x^3
phase_line(
    axes[1],
    fixed_points=[-1, 0, 1],
    stability=["estable", "inestable", "estable"],
    intervals=[(-3, -1, +1), (-1, 0, -1), (0, 1, +1), (1, 3, -1)],
    xlim=(-3, 3),
    title=r"Retrato de fase: $\dot{x}=x-x^3$"
)

# 3) dx/dt = 1 - 2 cos x en un período [0, 2pi]
pi = np.pi
fixed = [pi/3, 5*pi/3]
phase_line(
    axes[2],
    fixed_points=fixed,
    stability=["inestable", "estable"],
    intervals=[(0, pi/3, -1), (pi/3, 5*pi/3, +1), (5*pi/3, 2*pi, -1)],
    xlim=(0, 2*pi),
    title=r"Retrato de fase: $\dot{x}=1-2\cos x$, en $[0,2\pi)$"
)

axes[2].set_xticks([0, pi/3, pi, 5*pi/3, 2*pi])
axes[2].set_xticklabels(
    [r"$0$", r"$\pi/3$", r"$\pi$", r"$5\pi/3$", r"$2\pi$"]
)

# Leyenda manual
axes[0].scatter([], [], s=100, facecolors="black", edgecolors="black", label="estable")
axes[0].scatter([], [], s=100, facecolors="white", edgecolors="black", label="inestable")
axes[0].legend(loc="upper right")

plt.tight_layout()
plt.savefig("/mnt/data/retratos_fase_1d.png", dpi=200, bbox_inches="tight")
plt.show()
