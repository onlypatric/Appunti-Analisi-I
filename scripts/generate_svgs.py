from __future__ import annotations

import math
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "plots"


def setup_style() -> None:
    mpl.rcParams.update(
        {
            "figure.dpi": 120,
            "savefig.dpi": 120,
            "font.size": 11,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "legend.frameon": False,
        }
    )


def save_svg(fig: plt.Figure, name: str) -> Path:
    path = OUT_DIR / name
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, format="svg")
    plt.close(fig)
    return path


def plot_sin_over_x() -> None:
    x = np.linspace(-10, 10, 2001)
    y = np.divide(np.sin(x), x, out=np.ones_like(x), where=~np.isclose(x, 0.0))

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x, y, label=r"$\frac{\sin x}{x}$")
    ax.axhline(1.0, color="black", linewidth=1.0, alpha=0.4, linestyle="--", label=r"$y=1$")
    ax.scatter([0.0], [1.0], s=30, zorder=3)
    ax.set_title(r"Limite notevole: $\sin x / x \to 1$ per $x\to 0$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-0.5, 1.2)
    ax.legend()
    save_svg(fig, "sin_over_x.svg")


def plot_sin_vs_x_near_zero() -> None:
    x = np.linspace(-1.2, 1.2, 801)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x, np.sin(x), label=r"$\sin x$")
    ax.plot(x, x, label=r"$x$", linestyle="--")
    ax.set_title(r"Equivalenza: $\sin x \sim x$ per $x\to 0$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    save_svg(fig, "sin_vs_x_near_0.svg")


def plot_one_minus_cos_vs_x2_over_2() -> None:
    x = np.linspace(-1.2, 1.2, 801)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x, 1 - np.cos(x), label=r"$1-\cos x$")
    ax.plot(x, (x**2) / 2, label=r"$x^2/2$", linestyle="--")
    ax.set_title(r"Equivalenza: $1-\cos x \sim x^2/2$ per $x\to 0$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    save_svg(fig, "one_minus_cos_vs_x2_over_2.svg")


def plot_uniform_continuity_counterexample_one_over_x() -> None:
    x = np.linspace(0.05, 1.0, 1000)
    y = 1 / x

    delta = 0.2
    x1 = delta / 2
    x2 = delta / 4
    y1 = 1 / x1
    y2 = 1 / x2

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x, y, label=r"$f(x)=1/x$ su $(0,1)$")
    ax.scatter([x1, x2], [y1, y2], s=40, zorder=3)
    ax.vlines([x2, x1], ymin=0, ymax=[y2, y1], colors="black", alpha=0.25, linewidth=1.0)
    ax.hlines([y1, y2], xmin=0, xmax=[x1, x2], colors="black", alpha=0.25, linewidth=1.0)
    ax.annotate(rf"$x={x1:.2f}$", (x1, y1), xytext=(10, -10), textcoords="offset points")
    ax.annotate(rf"$y={x2:.2f}$", (x2, y2), xytext=(10, -10), textcoords="offset points")
    ax.set_title(r"Non uniformità: su $(0,1)$ la funzione $1/x$ cambia molto vicino a 0")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(0, 25)
    ax.legend()
    save_svg(fig, "one_over_x_not_uniform_continuous.svg")


def plot_x2_not_uniform_continuous_on_R() -> None:
    x = np.linspace(-12, 12, 2000)
    y = x**2

    x1 = 10.0
    x2 = 10.1
    y1 = x1**2
    y2 = x2**2

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x, y, label=r"$f(x)=x^2$")
    ax.scatter([x1, x2], [y1, y2], s=40, zorder=3)
    ax.annotate(r"$x=10$", (x1, y1), xytext=(8, -10), textcoords="offset points")
    ax.annotate(r"$x=10.1$", (x2, y2), xytext=(8, -10), textcoords="offset points")
    ax.set_title(r"$x^2$ non è uniformemente continua su tutto $R$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(0, 150)
    ax.legend()
    save_svg(fig, "x2_not_uniform_continuous_on_R.svg")


def plot_removable_discontinuity() -> None:
    x_left = np.linspace(-1.5, 0.98, 600)
    x_right = np.linspace(1.02, 3.5, 600)
    y_left = x_left + 1
    y_right = x_right + 1

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x_left, y_left, label=r"$f(x)=\frac{x^2-1}{x-1}$ per $x\ne 1$")
    ax.plot(x_right, y_right)
    ax.scatter([1.0], [2.0], s=60, facecolors="none", edgecolors="C0", linewidth=2, zorder=4)
    ax.scatter([1.0], [0.0], s=60, color="C1", zorder=4, label=r"valore definito $f(1)=0$")
    ax.axvline(1.0, color="black", linewidth=1.0, alpha=0.25, linestyle="--")
    ax.set_title("Discontinuità rimovibile: buco nel grafico")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-1, 5)
    ax.legend()
    save_svg(fig, "removable_discontinuity_hole.svg")


def plot_floor_near_zero() -> None:
    x = np.linspace(-2.0, 2.0, 2001)
    y = np.floor(x)

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.step(x, y, where="post", label=r"$\lfloor x\rfloor$")
    ax.scatter([0.0], [-1.0], s=60, facecolors="none", edgecolors="C0", linewidth=2, zorder=4)
    ax.scatter([0.0], [0.0], s=60, color="C0", zorder=4)
    ax.set_title("Discontinuità a salto: parte intera in 0")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-3, 3)
    ax.legend()
    save_svg(fig, "floor_jump_at_0.svg")


def plot_one_over_x_around_zero() -> None:
    x1 = np.linspace(-2.0, -0.05, 800)
    x2 = np.linspace(0.05, 2.0, 800)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x1, 1 / x1, label=r"$f(x)=1/x$")
    ax.plot(x2, 1 / x2)
    ax.axvline(0.0, color="black", linewidth=1.0, alpha=0.35, linestyle="--", label="asintoto $x=0$")
    ax.set_title("Discontinuità essenziale: asintoto verticale per $1/x$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-10, 10)
    ax.legend()
    save_svg(fig, "one_over_x_vertical_asymptote.svg")


def plot_sin_one_over_x_near_zero() -> None:
    x1 = np.linspace(-0.2, -0.001, 4000)
    x2 = np.linspace(0.001, 0.2, 4000)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x1, np.sin(1 / x1), linewidth=1.0, label=r"$\sin(1/x)$")
    ax.plot(x2, np.sin(1 / x2), linewidth=1.0)
    ax.axvline(0.0, color="black", linewidth=1.0, alpha=0.25, linestyle="--")
    ax.set_title(r"Limite che non esiste: $\sin(1/x)$ oscilla per $x\to 0$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-1.2, 1.2)
    ax.legend()
    save_svg(fig, "sin_one_over_x_oscillation.svg")


def plot_x2_sin_one_over_x_near_zero() -> None:
    x1 = np.linspace(-0.2, -0.001, 6000)
    x2 = np.linspace(0.001, 0.2, 6000)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x1, x1**2 * np.sin(1 / x1), linewidth=1.0, label=r"$x^2\sin(1/x)$")
    ax.plot(x2, x2**2 * np.sin(1 / x2), linewidth=1.0)
    ax.plot(np.concatenate([x1, x2]), np.concatenate([x1**2, x2**2]), color="black", alpha=0.35, linestyle="--", label=r"$\pm x^2$")
    ax.plot(np.concatenate([x1, x2]), np.concatenate([-x1**2, -x2**2]), color="black", alpha=0.35, linestyle="--")
    ax.axvline(0.0, color="black", linewidth=1.0, alpha=0.15, linestyle="--")
    ax.set_title(r"Carabinieri: $x^2\sin(1/x)\to 0$ per $x\to 0$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-0.05, 0.05)
    ax.legend()
    save_svg(fig, "x2_sin_one_over_x_squeeze.svg")


def plot_abs_x_cusp() -> None:
    x = np.linspace(-2.0, 2.0, 1000)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x, np.abs(x), label=r"$|x|$")
    ax.set_title(r"$|x|$ è continua ma non derivabile in $0$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.scatter([0.0], [0.0], s=40, zorder=3)
    ax.legend()
    save_svg(fig, "abs_x_cusp.svg")


def plot_sqrt_on_0_1() -> None:
    x = np.linspace(0.0, 1.0, 500)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x, np.sqrt(x), label=r"$\sqrt{x}$ su $[0,1]$")
    ax.set_title(r"Esempio: $\sqrt{x}$ è uniformemente continua su $[0,1]$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.1)
    ax.legend()
    save_svg(fig, "sqrt_on_0_1_uniform_continuous.svg")


def _style_axes(ax: plt.Axes) -> None:
    ax.axhline(0.0, color="black", linewidth=1.0, alpha=0.25)
    ax.axvline(0.0, color="black", linewidth=1.0, alpha=0.25)


def plot_venn_union_intersection() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.6))
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_xlim(-2.2, 2.2)
        ax.set_ylim(-1.7, 1.7)
        ax.axis("off")

    # Union shading (left)
    ax = axes[0]
    ax.add_patch(Circle((-0.7, 0.0), 1.2, fill=True, alpha=0.18, color="C0"))
    ax.add_patch(Circle((0.7, 0.0), 1.2, fill=True, alpha=0.18, color="C1"))
    ax.add_patch(Circle((-0.7, 0.0), 1.2, fill=False, linewidth=2.0, edgecolor="C0"))
    ax.add_patch(Circle((0.7, 0.0), 1.2, fill=False, linewidth=2.0, edgecolor="C1"))
    ax.text(-1.5, 1.25, "A", fontsize=12)
    ax.text(1.35, 1.25, "B", fontsize=12)
    ax.set_title(r"Unione: $A\cup B$")

    # Intersection shading (right)
    ax = axes[1]
    ax.add_patch(Circle((-0.7, 0.0), 1.2, fill=True, alpha=0.18, color="C0"))
    ax.add_patch(Circle((0.7, 0.0), 1.2, fill=True, alpha=0.18, color="C1"))
    # Repaint outside overlap with white rectangles to emphasize the intersection area.
    ax.add_patch(Rectangle((-2.2, -1.7), 1.05, 3.4, color="white", zorder=2))
    ax.add_patch(Rectangle((1.15, -1.7), 1.05, 3.4, color="white", zorder=2))
    ax.add_patch(Circle((-0.7, 0.0), 1.2, fill=False, linewidth=2.0, edgecolor="C0"))
    ax.add_patch(Circle((0.7, 0.0), 1.2, fill=False, linewidth=2.0, edgecolor="C1"))
    ax.text(-1.5, 1.25, "A", fontsize=12)
    ax.text(1.35, 1.25, "B", fontsize=12)
    ax.set_title(r"Intersezione: $A\cap B$")

    save_svg(fig, "venn_union_intersection.svg")


def plot_relation_digraph_example() -> None:
    points = [1, 2, 3]
    coords = {1: (-1.0, 0.0), 2: (0.0, 1.0), 3: (1.0, 0.0)}
    edges = [(1, 2), (2, 3), (2, 2)]

    fig, ax = plt.subplots(figsize=(5.8, 3.6))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(r"Esempio di relazione come digrafo su $A=\{1,2,3\}$")

    for p in points:
        x, y = coords[p]
        ax.scatter([x], [y], s=250, color="white", edgecolors="black", zorder=3)
        ax.text(x, y, str(p), ha="center", va="center", fontsize=12, zorder=4)

    def arrow(a: int, b: int, rad: float = 0.0) -> None:
        x1, y1 = coords[a]
        x2, y2 = coords[b]
        patch = FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=1.6,
            color="C0",
            connectionstyle=f"arc3,rad={rad}",
            zorder=2,
        )
        ax.add_patch(patch)

    arrow(1, 2, rad=0.15)
    arrow(2, 3, rad=0.15)
    arrow(2, 2, rad=0.6)
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-0.8, 1.6)
    save_svg(fig, "relation_digraph_example.svg")


def plot_hasse_divisibility_12() -> None:
    # Poset (A,|) where A = {1,2,3,4,6,12}
    coords = {
        1: (0.0, 0.0),
        2: (-0.8, 1.0),
        3: (0.8, 1.0),
        4: (-0.8, 2.0),
        6: (0.8, 2.0),
        12: (0.0, 3.0),
    }
    covers = [(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 12), (6, 12)]

    fig, ax = plt.subplots(figsize=(6.0, 3.8))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(r"Diagramma di Hasse per la divisibilità su $\{1,2,3,4,6,12\}$")

    for a, b in covers:
        x1, y1 = coords[a]
        x2, y2 = coords[b]
        ax.plot([x1, x2], [y1, y2], color="black", linewidth=1.4, alpha=0.8, zorder=1)

    for node, (x, y) in coords.items():
        ax.scatter([x], [y], s=260, color="white", edgecolors="black", zorder=3)
        ax.text(x, y, str(node), ha="center", va="center", fontsize=12, zorder=4)

    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-0.4, 3.4)
    save_svg(fig, "hasse_divisibility_12.svg")


def plot_function_mapping_injective_surjective() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 3.6))
    for ax in axes:
        ax.axis("off")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

    def draw_mapping(ax: plt.Axes, title: str, left: list[str], right: list[str], arrows: list[tuple[int, int]]) -> None:
        ax.set_title(title)
        left_x, right_x = 2.5, 7.5
        left_y = np.linspace(8, 2, len(left))
        right_y = np.linspace(8, 2, len(right))

        for i, label in enumerate(left):
            ax.scatter([left_x], [left_y[i]], s=220, color="white", edgecolors="black", zorder=3)
            ax.text(left_x, left_y[i], label, ha="center", va="center", fontsize=11)
        for j, label in enumerate(right):
            ax.scatter([right_x], [right_y[j]], s=220, color="white", edgecolors="black", zorder=3)
            ax.text(right_x, right_y[j], label, ha="center", va="center", fontsize=11)

        ax.text(left_x, 9.4, "A", ha="center", fontsize=12)
        ax.text(right_x, 9.4, "B", ha="center", fontsize=12)

        for i, j in arrows:
            patch = FancyArrowPatch(
                (left_x + 0.35, float(left_y[i])),
                (right_x - 0.35, float(right_y[j])),
                arrowstyle="-|>",
                mutation_scale=12,
                linewidth=1.5,
                color="C0",
                zorder=2,
            )
            ax.add_patch(patch)

    draw_mapping(
        axes[0],
        "Iniettiva (non suriettiva)",
        left=["1", "2", "3"],
        right=["a", "b", "c", "d"],
        arrows=[(0, 0), (1, 2), (2, 3)],
    )
    draw_mapping(
        axes[1],
        "Suriettiva (non iniettiva)",
        left=["1", "2", "3", "4"],
        right=["a", "b", "c"],
        arrows=[(0, 0), (1, 1), (2, 1), (3, 2)],
    )

    save_svg(fig, "function_mapping_injective_surjective.svg")


def plot_sequence_1_over_n() -> None:
    n = np.arange(1, 41)
    a = 1 / n
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.stem(n, a, basefmt=" ", linefmt="C0-", markerfmt="C0o")
    ax.axhline(0.0, color="black", linewidth=1.0, alpha=0.25)
    ax.set_title(r"Successione: $a_n=1/n\to 0$")
    ax.set_xlabel("n")
    ax.set_ylabel(r"$a_n$")
    ax.set_ylim(-0.05, 1.05)
    save_svg(fig, "sequence_1_over_n.svg")


def plot_sequence_minus1_pow_n() -> None:
    n = np.arange(1, 31)
    a = (-1) ** n
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.stem(n, a, basefmt=" ", linefmt="C1-", markerfmt="C1o")
    ax.axhline(0.0, color="black", linewidth=1.0, alpha=0.25)
    ax.set_title(r"Successione: $a_n=(-1)^n$ (oscilla, non converge)")
    ax.set_xlabel("n")
    ax.set_ylabel(r"$a_n$")
    ax.set_ylim(-1.3, 1.3)
    save_svg(fig, "sequence_minus1_pow_n.svg")


def plot_sequence_geometric_half() -> None:
    n = np.arange(0, 21)
    a = (1 / 2) ** n
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.stem(n, a, basefmt=" ", linefmt="C2-", markerfmt="C2o")
    ax.axhline(0.0, color="black", linewidth=1.0, alpha=0.25)
    ax.set_title(r"Successione geometrica: $a_n=(1/2)^n\to 0$")
    ax.set_xlabel("n")
    ax.set_ylabel(r"$a_n$")
    ax.set_ylim(-0.05, 1.05)
    save_svg(fig, "sequence_geometric_half.svg")


def plot_partial_sums_harmonic() -> None:
    n = np.arange(1, 101)
    s = np.cumsum(1 / n)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(n, s, label=r"$s_n=\sum_{k=1}^n 1/k$")
    ax.set_title(r"Somme parziali armoniche (crescono, divergenza lenta)")
    ax.set_xlabel("n")
    ax.set_ylabel(r"$s_n$")
    ax.legend()
    save_svg(fig, "partial_sums_harmonic.svg")


def plot_tangent_x2_at_1() -> None:
    x = np.linspace(-0.2, 2.2, 800)
    y = x**2
    x0 = 1.0
    y0 = x0**2
    m = 2 * x0
    tangent = y0 + m * (x - x0)

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x, y, label=r"$f(x)=x^2$")
    ax.plot(x, tangent, linestyle="--", label=r"tangente in $x_0=1$: $y=2(x-1)+1$")
    ax.scatter([x0], [y0], s=50, zorder=4)
    _style_axes(ax)
    ax.set_title(r"Derivata come pendenza della tangente")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-0.5, 5.0)
    ax.legend()
    save_svg(fig, "tangent_x2_at_1.svg")


def plot_taylor_sin_approximations() -> None:
    x = np.linspace(-2.5, 2.5, 1200)
    f = np.sin(x)
    p1 = x
    p3 = x - (x**3) / 6
    p5 = x - (x**3) / 6 + (x**5) / 120

    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.plot(x, f, label=r"$\sin x$")
    ax.plot(x, p1, linestyle="--", label=r"Taylor ordine 1")
    ax.plot(x, p3, linestyle="--", label=r"Taylor ordine 3")
    ax.plot(x, p5, linestyle="--", label=r"Taylor ordine 5")
    ax.set_title(r"Approssimazioni di Taylor per $\sin x$ in 0")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-2.0, 2.0)
    ax.legend(ncols=2)
    save_svg(fig, "taylor_sin_approximations.svg")


def plot_taylor_exp_approximations() -> None:
    x = np.linspace(-2.0, 2.0, 1200)
    f = np.exp(x)
    p1 = 1 + x
    p2 = 1 + x + (x**2) / 2
    p3 = 1 + x + (x**2) / 2 + (x**3) / 6
    p4 = 1 + x + (x**2) / 2 + (x**3) / 6 + (x**4) / 24

    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.plot(x, f, label=r"$e^x$")
    ax.plot(x, p1, linestyle="--", label="ordine 1")
    ax.plot(x, p2, linestyle="--", label="ordine 2")
    ax.plot(x, p3, linestyle="--", label="ordine 3")
    ax.plot(x, p4, linestyle="--", label="ordine 4")
    ax.set_title(r"Approssimazioni di Taylor per $e^x$ in 0")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-0.5, 8.0)
    ax.legend(ncols=2)
    save_svg(fig, "taylor_exp_approximations.svg")


def plot_riemann_sum_x2_0_1_n4() -> None:
    a, b = 0.0, 1.0
    n = 4
    xs = np.linspace(a, b, 400)
    f = xs**2
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(xs, f, label=r"$f(x)=x^2$")

    dx = (b - a) / n
    for k in range(n):
        xk = a + k * dx
        height = xk**2  # left Riemann sum
        rect = Rectangle((xk, 0.0), dx, height, facecolor="C0", alpha=0.18, edgecolor="C0")
        ax.add_patch(rect)

    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.set_title(r"Somma di Riemann (sinistra) per $\int_0^1 x^2\,dx$ con $n=4$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    save_svg(fig, "riemann_sum_x2_0_1_n4.svg")


def plot_area_between_curves_x_and_x2() -> None:
    x = np.linspace(0.0, 1.0, 600)
    f = x
    g = x**2
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x, f, label=r"$f(x)=x$")
    ax.plot(x, g, label=r"$g(x)=x^2$")
    ax.fill_between(x, g, f, alpha=0.18, color="C2", label="area tra le curve")
    ax.set_title(r"Area tra $x$ e $x^2$ su $[0,1]$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.legend()
    save_svg(fig, "area_between_x_and_x2.svg")


def plot_improper_integral_one_over_sqrt_x() -> None:
    x = np.linspace(1e-3, 1.0, 2000)
    y = 1 / np.sqrt(x)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(x, y, label=r"$f(x)=1/\sqrt{x}$")
    ax.set_title(r"Singolarità integrabile: $\int_0^1 x^{-1/2}\,dx$ converge")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(0.0, 35.0)
    ax.legend()
    save_svg(fig, "improper_one_over_sqrt_x.svg")


def plot_slope_field_yprime_equals_y() -> None:
    # y' = y
    x = np.linspace(-2.0, 2.0, 17)
    y = np.linspace(-2.0, 2.0, 17)
    X, Y = np.meshgrid(x, y)
    S = Y
    U = np.ones_like(S)
    V = S
    N = np.sqrt(U**2 + V**2)
    U /= N
    V /= N

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.quiver(X, Y, U, V, angles="xy", pivot="middle", width=0.0032, alpha=0.6)

    xs = np.linspace(-2.0, 2.0, 300)
    for y0 in [-1.5, -0.8, 0.5, 1.2]:
        ax.plot(xs, y0 * np.exp(xs), linewidth=1.4, label=rf"$y(0)={y0}$")

    _style_axes(ax)
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.0, 2.0)
    ax.set_title(r"Campo di direzioni per $y'=y$ e alcune soluzioni")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(ncols=2, fontsize=9)
    save_svg(fig, "slope_field_yprime_equals_y.svg")


def plot_phase_line_logistic() -> None:
    # y' = y(1-y)
    fig, ax = plt.subplots(figsize=(6.0, 2.6))
    ax.axis("off")
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.6, 0.6)
    ax.set_title(r"Linea delle fasi per $y'=y(1-y)$")

    ax.plot([0.0, 1.0], [0.0, 0.0], color="black", linewidth=2)
    ax.scatter([0.0, 1.0], [0.0, 0.0], s=70, color="black")
    ax.text(0.0, 0.18, r"$0$", ha="center")
    ax.text(1.0, 0.18, r"$1$", ha="center")

    # arrows: (-inf,0): left; (0,1): right; (1,inf): left
    ax.annotate("", xy=(-0.12, 0.0), xytext=(0.12, 0.0), arrowprops={"arrowstyle": "<|-", "lw": 1.6})
    ax.annotate("", xy=(0.82, 0.0), xytext=(0.18, 0.0), arrowprops={"arrowstyle": "-|>", "lw": 1.6})
    ax.annotate("", xy=(1.12, 0.0), xytext=(0.88, 0.0), arrowprops={"arrowstyle": "<|-", "lw": 1.6})

    ax.text(0.5, -0.28, r"$y'>0$", ha="center", fontsize=11)
    ax.text(-0.02, -0.28, r"$y'<0$", ha="right", fontsize=11)
    ax.text(1.02, -0.28, r"$y'<0$", ha="left", fontsize=11)
    save_svg(fig, "phase_line_logistic.svg")


def study_01_x2_over_x_minus_1() -> None:
    x_left = np.linspace(-6, 0.98, 2000)
    x_right = np.linspace(1.02, 8, 2400)
    f_left = (x_left**2) / (x_left - 1)
    f_right = (x_right**2) / (x_right - 1)

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(x_left, f_left, label=r"$f(x)=\frac{x^2}{x-1}$")
    ax.plot(x_right, f_right)
    _style_axes(ax)
    ax.axvline(1.0, color="black", alpha=0.35, linestyle="--", label=r"asintoto $x=1$")
    x = np.linspace(-6, 8, 400)
    ax.plot(x, x + 1, color="black", alpha=0.35, linestyle="--", label=r"asintoto $y=x+1$")
    ax.scatter([0.0, 2.0], [0.0, 4.0], s=50, zorder=4)
    ax.set_xlim(-6, 8)
    ax.set_ylim(-20, 20)
    ax.set_title(r"Studio 01: $f(x)=x^2/(x-1)$")
    ax.legend()
    save_svg(fig, "studi-di-funzione/studio-01-x2-su-x-meno-1.svg")


def study_02_x2_minus_4_over_x2_minus_1() -> None:
    x1 = np.linspace(-6, -1.02, 2000)
    x2 = np.linspace(-0.98, 0.98, 2000)
    x3 = np.linspace(1.02, 6, 2000)
    f = lambda t: (t**2 - 4) / (t**2 - 1)

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(x1, f(x1), label=r"$f(x)=\frac{x^2-4}{x^2-1}$")
    ax.plot(x2, f(x2))
    ax.plot(x3, f(x3))
    _style_axes(ax)
    ax.axvline(-1.0, color="black", alpha=0.35, linestyle="--", label=r"asintoti $x=\pm1$")
    ax.axvline(1.0, color="black", alpha=0.35, linestyle="--")
    ax.axhline(1.0, color="black", alpha=0.35, linestyle="--", label=r"asintoto $y=1$")
    ax.scatter([-2.0, 2.0, 0.0], [0.0, 0.0, 4.0], s=50, zorder=4)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 8)
    ax.set_title(r"Studio 02: $(x^2-4)/(x^2-1)$")
    ax.legend()
    save_svg(fig, "studi-di-funzione/studio-02-x2-meno-4-su-x2-meno-1.svg")


def study_03_x3_minus_3x_over_x2_plus_1() -> None:
    x = np.linspace(-8, 8, 4000)
    y = (x**3 - 3 * x) / (x**2 + 1)

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(x, y, label=r"$f(x)=\frac{x^3-3x}{x^2+1}$")
    _style_axes(ax)
    ax.plot(x, x, color="black", alpha=0.35, linestyle="--", label=r"asintoto $y=x$")
    zeros = [-math.sqrt(3), 0.0, math.sqrt(3)]
    ax.scatter(zeros, [0.0, 0.0, 0.0], s=45, zorder=4)
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_title(r"Studio 03: $(x^3-3x)/(x^2+1)$")
    ax.legend()
    save_svg(fig, "studi-di-funzione/studio-03-x3-meno-3x-su-x2-piu-1.svg")


def study_04_ln_x_over_x() -> None:
    x = np.linspace(0.05, 10.0, 3000)
    y = np.log(x) / x

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(x, y, label=r"$f(x)=\frac{\ln x}{x}$")
    ax.axhline(0.0, color="black", linewidth=1.0, alpha=0.25)
    ax.axvline(0.0, color="black", linewidth=1.0, alpha=0.25)
    ax.scatter([1.0, math.e], [0.0, 1 / math.e], s=50, zorder=4)
    ax.annotate(r"$x=1$", (1.0, 0.0), xytext=(8, 8), textcoords="offset points")
    ax.annotate(r"$x=e$", (math.e, 1 / math.e), xytext=(8, -14), textcoords="offset points")
    ax.set_xlim(0, 10)
    ax.set_ylim(-6, 1)
    ax.set_title(r"Studio 04: $\ln(x)/x$ su $(0,+\infty)$")
    ax.legend()
    save_svg(fig, "studi-di-funzione/studio-04-ln-x-su-x.svg")


def study_05_sqrt_x_over_x_plus_1() -> None:
    x = np.linspace(0.0, 10.0, 2000)
    y = np.sqrt(x) / (x + 1)

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(x, y, label=r"$f(x)=\frac{\sqrt{x}}{x+1}$")
    ax.axhline(0.0, color="black", linewidth=1.0, alpha=0.25)
    ax.axvline(0.0, color="black", linewidth=1.0, alpha=0.25)
    ax.scatter([0.0, 1.0], [0.0, 0.5], s=50, zorder=4)
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.1, 0.8)
    ax.set_title(r"Studio 05: $\sqrt{x}/(x+1)$ su $[0,+\infty)$")
    ax.legend()
    save_svg(fig, "studi-di-funzione/studio-05-radice-x-su-x-piu-1.svg")


def study_06_abs_x_over_x_plus_1() -> None:
    x1 = np.linspace(-8, -1.02, 2000)
    x2 = np.linspace(-0.98, 8, 3000)
    f = lambda t: np.abs(t) / (t + 1)

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(x1, f(x1), label=r"$f(x)=\frac{|x|}{x+1}$")
    ax.plot(x2, f(x2))
    _style_axes(ax)
    ax.axvline(-1.0, color="black", alpha=0.35, linestyle="--", label=r"asintoto $x=-1$")
    ax.axhline(1.0, color="black", alpha=0.25, linestyle="--", label=r"$y=1$")
    ax.axhline(-1.0, color="black", alpha=0.25, linestyle="--", label=r"$y=-1$")
    ax.scatter([0.0], [0.0], s=50, zorder=4)
    ax.set_xlim(-8, 8)
    ax.set_ylim(-6, 6)
    ax.set_title(r"Studio 06: $|x|/(x+1)$")
    ax.legend(ncols=3)
    save_svg(fig, "studi-di-funzione/studio-06-modulo-x-su-x-piu-1.svg")


def study_07_exp_minus_x2() -> None:
    x = np.linspace(-3.5, 3.5, 2000)
    y = np.exp(-x**2)

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(x, y, label=r"$f(x)=e^{-x^2}$")
    _style_axes(ax)
    ax.axhline(0.0, color="black", alpha=0.25, linestyle="--", label=r"asintoto $y=0$")
    ax.scatter([0.0], [1.0], s=50, zorder=4)
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-0.1, 1.1)
    ax.set_title(r"Studio 07: $e^{-x^2}$")
    ax.legend()
    save_svg(fig, "studi-di-funzione/studio-07-exp-meno-x2.svg")


def study_08_arctan_x() -> None:
    x = np.linspace(-10, 10, 2000)
    y = np.arctan(x)

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(x, y, label=r"$f(x)=\arctan x$")
    _style_axes(ax)
    ax.axhline(math.pi / 2, color="black", alpha=0.35, linestyle="--", label=r"asintoti $y=\pm\pi/2$")
    ax.axhline(-math.pi / 2, color="black", alpha=0.35, linestyle="--")
    ax.scatter([0.0], [0.0], s=50, zorder=4)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-2.0, 2.0)
    ax.set_title(r"Studio 08: $\arctan x$")
    ax.legend()
    save_svg(fig, "studi-di-funzione/studio-08-arctan-x.svg")


def study_09_sin_x_over_x_extended() -> None:
    x = np.linspace(-20, 20, 6000)
    y = np.divide(np.sin(x), x, out=np.ones_like(x), where=~np.isclose(x, 0.0))

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(x, y, label=r"$f(x)=\sin x/x$ (con $f(0)=1$)")
    _style_axes(ax)
    ax.axhline(0.0, color="black", alpha=0.25, linestyle="--", label=r"asintoto $y=0$")
    ax.scatter([0.0], [1.0], s=50, zorder=4)
    ax.set_xlim(-20, 20)
    ax.set_ylim(-0.4, 1.2)
    ax.set_title(r"Studio 09: $\sin x/x$ estesa in $0$")
    ax.legend()
    save_svg(fig, "studi-di-funzione/studio-09-sin-x-su-x.svg")


def study_10_x_minus_1_over_x2_plus_1() -> None:
    x = np.linspace(-6, 6, 2000)
    y = (x - 1) / (x**2 + 1)

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(x, y, label=r"$f(x)=\frac{x-1}{x^2+1}$")
    _style_axes(ax)
    ax.axhline(0.0, color="black", alpha=0.25, linestyle="--", label=r"asintoto $y=0$")
    ax.scatter([1.0], [0.0], s=50, zorder=4)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-1.0, 1.0)
    ax.set_title(r"Studio 10: $(x-1)/(x^2+1)$")
    ax.legend()
    save_svg(fig, "studi-di-funzione/studio-10-x-meno-1-su-x2-piu-1.svg")


def main() -> None:
    setup_style()
    plot_sin_over_x()
    plot_sin_vs_x_near_zero()
    plot_one_minus_cos_vs_x2_over_2()
    plot_venn_union_intersection()
    plot_relation_digraph_example()
    plot_hasse_divisibility_12()
    plot_function_mapping_injective_surjective()
    plot_sequence_1_over_n()
    plot_sequence_minus1_pow_n()
    plot_sequence_geometric_half()
    plot_partial_sums_harmonic()
    plot_uniform_continuity_counterexample_one_over_x()
    plot_x2_not_uniform_continuous_on_R()
    plot_removable_discontinuity()
    plot_floor_near_zero()
    plot_one_over_x_around_zero()
    plot_sin_one_over_x_near_zero()
    plot_x2_sin_one_over_x_near_zero()
    plot_abs_x_cusp()
    plot_sqrt_on_0_1()
    plot_tangent_x2_at_1()
    plot_taylor_sin_approximations()
    plot_taylor_exp_approximations()
    plot_riemann_sum_x2_0_1_n4()
    plot_area_between_curves_x_and_x2()
    plot_improper_integral_one_over_sqrt_x()
    plot_slope_field_yprime_equals_y()
    plot_phase_line_logistic()
    study_01_x2_over_x_minus_1()
    study_02_x2_minus_4_over_x2_minus_1()
    study_03_x3_minus_3x_over_x2_plus_1()
    study_04_ln_x_over_x()
    study_05_sqrt_x_over_x_plus_1()
    study_06_abs_x_over_x_plus_1()
    study_07_exp_minus_x2()
    study_08_arctan_x()
    study_09_sin_x_over_x_extended()
    study_10_x_minus_1_over_x2_plus_1()
    print(f"Generated SVGs in: {OUT_DIR}")


if __name__ == "__main__":
    main()
