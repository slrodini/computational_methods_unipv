import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

theta = 0.5


def f(z):
    return (1 + z * (1 - theta)) / (1 - theta * z)


Nx, Ny = 600, 600
x = np.linspace(-10, 10, Nx)  # Re(z)
y = np.linspace(-10, 10, Ny)  # Im(z)

X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

F = f(Z)
absF = np.abs(F)


color_value = np.empty_like(absF)

mask1 = absF <= 1
mask2 = (absF > 1) & (absF < 2)
mask3 = absF >= 2

color_value[mask1] = 0.5 * absF[mask1]
color_value[mask2] = 0.5 + 0.5 * (absF[mask2] - 1.0)
color_value[mask3] = 1.0

cmap = LinearSegmentedColormap.from_list(
    "blue_white_red",
    [
        (0.0, "#0000aa"),  # deep blue
        (0.5, "#ffffff"),  # white at |f| = 1
        (1.0, "#aa0000"),  # deep red
    ],
)

plt.figure(figsize=(6, 6))
im = plt.imshow(
    color_value,
    extent=[x.min(), x.max(), y.min(), y.max()],
    origin="lower",
    cmap=cmap,
    interpolation="nearest",
    aspect="equal",
    vmin=0,
    vmax=1,
)

plt.xlabel(r"$\Re(z)$")
plt.ylabel(r"$\Im(z)$")
plt.title(r"R(z)")

# Optional colorbar with physical labels
cbar = plt.colorbar(im)
cbar.set_label(r"$|f(z)|$")
cbar.set_ticks([0.0, 0.5, 1.0])
cbar.set_ticklabels(["0", "1", ">=2"])

plt.show()
