"""Generate the PET coincidence geometry used in lecture 9."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots(figsize=(8, 4.1), layout="constrained")
ax.add_patch(Circle((0, 0), 1, fill=False, ec="#526876", lw=2))
ax.axhline(0, xmin=.19, xmax=.81, color="#157a80", lw=2)
ax.plot([-.05, .55], [0, 0], lw=21, alpha=.19, color="#157a80",
        solid_capstyle="round")
ax.scatter([-1, 1], [0, 0], marker="s", s=200, color="#173f58", zorder=4)
ax.scatter(.25, 0, s=70, color="#bd4b46", zorder=5)
for endpoint in (-.75, .78):
    ax.annotate("", (endpoint, 0), (.25, 0),
                arrowprops={"arrowstyle": "-|>", "color": "#157a80", "lw": 2})
ax.text(-1.1, .14, "Detector A", ha="right", fontsize=13)
ax.text(1.1, .14, "Detector B", ha="left", fontsize=13)
ax.annotate("Annihilation", (.25, .04), (.32, .51), ha="center", fontsize=13,
            arrowprops={"arrowstyle": "-", "color": "#bd4b46"})
ax.text(0, -.25, "Line of response", ha="center", fontsize=13)
ax.text(0, -1.15, "Arrival-time difference favors a region along the line.",
        ha="center", fontsize=12, color="#526876")
ax.set(xlim=(-1.68, 1.68), ylim=(-1.28, 1.09), aspect="equal")
ax.axis("off")
fig.savefig(Path(__file__).with_name("09_pet_coincidence.pdf"), bbox_inches="tight")
