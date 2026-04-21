import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


# ---------------------------------
# Define your complex functions here
# ---------------------------------
def f(z):
    return 1 + z


def g(z):
    return 1 + z + z * z / 2 + z * z * z / 6 * z * z * z * z / 24


# ---------------------------------
# Map |h(z)| to color scale:
# 0   -> blue
# 1   -> white
# >=2 -> red
# ---------------------------------
def modulus_to_color_value(absH):
    color_value = np.empty_like(absH, dtype=float)

    mask1 = absH <= 1
    mask2 = (absH > 1) & (absH < 2)
    mask3 = absH >= 2

    # [0,1] -> [0,0.5]
    color_value[mask1] = 0.5 * absH[mask1]

    # [1,2] -> [0.5,1]
    color_value[mask2] = 0.5 + 0.5 * (absH[mask2] - 1.0)

    # >=2 -> 1
    color_value[mask3] = 1.0

    return color_value


# ---------------------------------
# Grid in the complex plane
# ---------------------------------
Nx, Ny = 600, 600
x = np.linspace(-3, 3, Nx)
y = np.linspace(-3, 3, Ny)

X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Evaluate the functions
F = f(Z)
G = g(Z)

absF = np.abs(F)
absG = np.abs(G)

# Convert to color values
colorF = modulus_to_color_value(absF)
colorG = modulus_to_color_value(absG)

# ---------------------------------
# Colormap: deep blue -> white -> deep red
# ---------------------------------
cmap = LinearSegmentedColormap.from_list(
    "blue_white_red",
    [
        (0.0, "#0000aa"),  # deep blue
        (0.5, "#ffffff"),  # white
        (1.0, "#aa0000"),  # deep red
    ],
)

# ---------------------------------
# Plot
# ---------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)

im1 = axes[0].imshow(
    colorF,
    extent=[x.min(), x.max(), y.min(), y.max()],
    origin="lower",
    cmap=cmap,
    aspect="equal",
    vmin=0,
    vmax=1,
)
axes[0].set_title(r"$1+z$")
axes[0].set_xlabel(r"$\Re(z)$")
axes[0].set_ylabel(r"$\Im(z)$")

im2 = axes[1].imshow(
    colorG,
    extent=[x.min(), x.max(), y.min(), y.max()],
    origin="lower",
    cmap=cmap,
    aspect="equal",
    vmin=0,
    vmax=1,
)
axes[1].set_title(r"Rk4th")
axes[1].set_xlabel(r"$\Re(z)$")
axes[1].set_ylabel(r"$\Im(z)$")

# Shared colorbar
cbar = fig.colorbar(im2, ax=axes, shrink=0.9)
cbar.set_label(r"$|h(z)|$")
cbar.set_ticks([0.0, 0.5, 1.0])
cbar.set_ticklabels(["0", "1", r"$\geq 2$"])

plt.show()
