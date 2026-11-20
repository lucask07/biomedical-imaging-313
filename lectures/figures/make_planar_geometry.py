"""Generate an ideal parallel-hole collimator diagram."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(9, 3.4), layout="constrained")
ax.add_patch(Rectangle((0, 2.2), 8, .45, color="#78bfc2"))
for i in range(9):
    ax.add_patch(Rectangle((i-.12, 1.1), .24, 1.1, color="#536473"))
ax.scatter([3.5], [0], color="#bd4b46", s=80, zorder=3)
for x in (3.35, 3.65):
    ax.annotate("", (x, 2.23), (3.5, .03),
                arrowprops={"arrowstyle":"-|>", "color":"#157a80", "lw":2})
ax.annotate("", (5.9, 1.1), (3.53, .015),
            arrowprops={"arrowstyle":"-|>", "color":"#ad591e", "lw":2})
ax.text(5.8, .44, "Stops at a septum", color="#ad591e", fontsize=14)
ax.text(4, 2.8, "Scintillator", ha="center", color="#173f58", fontsize=15)
ax.text(8.35, 1.64, "Collimator", va="center", color="#536473", fontsize=14)
ax.text(3.5, -.33, "Point source", ha="center", color="#bd4b46", fontsize=14)
ax.text(1.1, .44, "Accepted rays", color="#157a80", fontsize=14)
ax.set(xlim=(-.55, 10.2), ylim=(-.55, 3.1))
ax.axis("off")
fig.savefig(Path(__file__).with_name("08_parallel_holes.pdf"), bbox_inches="tight")
