"""Build synthetic X-ray transmission and parallel-beam CT teaching figures."""

from pathlib import Path
import os

LECTURES = Path(__file__).resolve().parent
OUT = LECTURES / "figures"
OUT.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(LECTURES.parent / "build/lectures/matplotlib"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter

BLUE, TEAL, GOLD = "#173F58", "#157A80", "#A86914"
plt.rcParams.update({
    "font.size": 16, "axes.titlesize": 17, "axes.labelsize": 16,
    "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42,
})


def save(fig, name):
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight", pad_inches=0.11)
    plt.close(fig)


def spectrum():
    energy = np.linspace(12, 80, 700)
    continuum = (80 - energy) * np.exp(-(26 / energy) ** 3) / energy
    peaks = sum(amplitude * np.exp(-0.5 * ((energy - center) / 0.40) ** 2)
                for center, amplitude in [(59.3, 1.20), (67.2, 0.64)])
    fig, ax = plt.subplots(figsize=(9.0, 2.4), layout="constrained")
    ax.plot(energy, continuum + peaks, color=TEAL, linewidth=2.4)
    ax.fill_between(energy, continuum, color=TEAL, alpha=0.18)
    ax.text(35, 0.97, "Bremsstrahlung", ha="center", color=BLUE)
    ax.annotate("Characteristic peaks", xy=(59.3, 1.51), xytext=(70, 1.67),
                ha="center", arrowprops={"arrowstyle": "-", "color": BLUE})
    ax.set(xlim=(10, 88), ylim=(0, 1.90), xlabel="Photon energy (keV)",
           ylabel="Relative output", yticks=[])
    ax.set_title("Illustrative filtered spectrum at 80 kVp", loc="left", color=BLUE)
    save(fig, "04_spectrum")


def transmission_examples():
    # A centered disk replaces some of the background along affected rays.
    pixel_mm = 0.25
    x = (np.arange(96) - 47.5) * pixel_mm
    xx, yy = np.meshgrid(x, x)
    insert = xx**2 + yy**2 <= 1.8**2

    def transmission(thickness):
        return np.exp(-0.025 * 30 - (0.055 - 0.025) * thickness * insert)

    def noisy(expected, incident, seed):
        return np.random.default_rng(seed).poisson(incident * expected) / incident

    def panels(name, arrays, titles, colors):
        fig, axes = plt.subplots(2, len(arrays), figsize=(11.2, 4.2),
                                 gridspec_kw={"height_ratios": [2.7, 1]}, layout="constrained")
        for col, (image, title, color) in enumerate(zip(arrays, titles, colors)):
            ax, profile = axes[:, col]
            ax.imshow(image, cmap="gray", vmin=0.18, vmax=0.70,
                      extent=(-12, 12, -12, 12), origin="lower", interpolation="nearest")
            ax.axhline(x[48], color=color, linewidth=0.9, alpha=0.9)
            ax.set_title(title)
            ax.set_axis_off()
            profile.plot(x, image[48], color=color, linewidth=1.6)
            profile.set(xlim=(-12, 12), ylim=(0.18, 0.70), xlabel="Position (mm)",
                        yticks=[0.2, 0.4, 0.6])
            profile.grid(alpha=0.2)
            if col == 0:
                profile.set_ylabel("Transmission")
        save(fig, name)

    thin, thick = transmission(4), transmission(12)
    panels("05_visibility", [thick, gaussian_filter(thick, 3), noisy(thick, 80, 313)],
           ["Expected transmission", "With detector blur", "With photon noise"], [TEAL, GOLD, BLUE])
    panels("05_thickness", [thin, thick], ["4 mm insert", "12 mm insert"], [TEAL, GOLD])
    panels("05_counts", [noisy(thin, 80, 313), noisy(thin, 320, 314)],
           ["80 incident photons/pixel", "320 incident photons/pixel"], [TEAL, BLUE])


def ct_examples():
    # Each disk adds a constant attenuation coefficient inside its boundary.
    # The ray integral through a disk is its chord length times that coefficient.
    disks = [(0, 0, 52, 0.019), (-13, 17, 9, 0.021), (-13, -17, 7, 0.010)]
    step = 0.50
    s = np.arange(-75, 75 + step, step)
    xx, yy = np.meshgrid(s, s)
    phantom = sum(mu * ((xx - x)**2 + (yy - y)**2 <= radius**2)
                  for x, y, radius, mu in disks)

    angles = np.arange(180)
    theta = np.deg2rad(angles)
    projections = sum(2 * mu * np.sqrt(np.maximum(
        radius**2 - (s[:, None] - x * np.cos(theta) - y * np.sin(theta))**2, 0))
        for x, y, radius, mu in disks)
    assert np.isclose(projections[len(s)//2, 0], 2 * 52 * 0.019)

    # Ramp filter in cycles/mm, with zero padding to limit periodic wraparound.
    n_fft = 1024
    padded = np.pad(projections, ((0, n_fft - len(s)), (0, 0)))
    ramp = np.abs(np.fft.rfftfreq(n_fft, d=step))[:, None]
    filtered = np.fft.irfft(np.fft.rfft(padded, axis=0) * ramp, axis=0)[:len(s)]

    def backproject(values, views):
        result = np.zeros_like(xx)
        for j in views:
            ray_coordinate = xx * np.cos(theta[j]) + yy * np.sin(theta[j])
            result += np.interp(ray_coordinate, s, values[:, j], left=0, right=0)
        return result * np.pi / len(views)

    roi = (xx - 19)**2 + yy**2 <= 6**2

    def scaled_backprojection(views):
        result = backproject(projections, views)
        return result * (0.019 / result[roi].mean())

    fbp = backproject(filtered, angles)
    assert abs(fbp[roi].mean() - 0.019) < 0.001
    assert fbp[np.unravel_index(np.argmax(phantom), phantom.shape)] > 0.026

    def ct_image(ax, values, title):
        ax.imshow(values, extent=(-75, 75, -75, 75), origin="lower",
                  cmap="gray", vmin=0, vmax=0.041, interpolation="nearest")
        ax.set(xlim=(-64, 64), ylim=(-64, 64), title=title)
        ax.set_axis_off()

    def compare(name, arrays, titles):
        fig, axes = plt.subplots(1, len(arrays), figsize=(10.8, 3.3),
                                 layout="constrained")
        for ax, values, title in zip(axes, arrays, titles):
            ct_image(ax, values, title)
        save(fig, name)

    fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.05), layout="constrained")
    ct_image(axes[0], phantom, "Slice with two inserts")
    for ax, j, title in zip(axes[1:], (0, 90), ("0°: inserts overlap", "90°: inserts separate")):
        ax.plot(s, projections[:, j], color=TEAL, linewidth=2)
        ax.set(xlabel="Detector position (mm)", xlim=(-60, 60), ylim=(0, 3),
               title=title, ylabel="Line integral")
        ax.grid(alpha=0.2)
    save(fig, "06_views")

    fig, ax = plt.subplots(figsize=(8.2, 3.65), layout="constrained")
    image = ax.imshow(projections, extent=(-0.5, 179.5, -75.25, 75.25),
                      origin="lower", cmap="magma", aspect="auto")
    ax.set(xlabel="View angle (degrees)", ylabel="Detector position (mm)",
           xticks=[0, 45, 90, 135, 179])
    fig.colorbar(image, ax=ax, label="Line integral")
    save(fig, "06_sinogram")

    compare("06_backprojection", [scaled_backprojection(np.arange(0, 180, stride))
                                  for stride in (180, 30, 3)],
            ["1 view", "6 views", "60 views"])
    compare("06_reconstruction", [phantom, scaled_backprojection(angles), fbp],
            ["Known object", "Unfiltered backprojection", "Filtered backprojection"])
    compare("06_few_views", [phantom, backproject(filtered, np.arange(0, 180, 15)), fbp],
            ["Known object", "12 views", "180 views"])


if __name__ == "__main__":
    spectrum()
    transmission_examples()
    ct_examples()
