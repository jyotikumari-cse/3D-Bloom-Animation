import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# Create figure
# -----------------------------
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection="3d")

ax.set_title("3D Flower", fontsize=22)

# -----------------------------
# Flower parameters
# -----------------------------
petals = 6

# Petal coordinates
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 1, 35)

U, V = np.meshgrid(u, v)

# -----------------------------
# Stem
# -----------------------------
t = np.linspace(0, 10, 150)

stem_x = 0.12 * np.sin(t)
stem_y = 0.12 * np.cos(t)
stem_z = t - 5

# -----------------------------
# Flower center
# -----------------------------
theta = np.linspace(0, 2 * np.pi, 100)
r = np.linspace(0, 0.8, 30)

T, R = np.meshgrid(theta, r)

center_x = R * np.cos(T)
center_y = R * np.sin(T)
center_z = 5 + 0.15 * np.sin(R * 8)

# -----------------------------
# Animation
# -----------------------------
def update(frame):

    ax.clear()

    # Camera
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-5, 6)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_title("3D Flower - Building & Rotating", fontsize=18)

    # --------------------------------
    # STEP 1: Build stem
    # --------------------------------
    stem_end = int(min(frame, 40) / 40 * len(t))

    if stem_end > 1:
        ax.plot3D(
            stem_x[:stem_end],
            stem_y[:stem_end],
            stem_z[:stem_end],
            linewidth=5
        )

    # --------------------------------
    # STEP 2: Build flower center
    # --------------------------------
    if frame >= 35:

        center_progress = min((frame - 35) / 25, 1)

        rows = max(1, int(center_progress * len(r)))

        ax.plot_surface(
            center_x[:rows],
            center_y[:rows],
            center_z[:rows],
            alpha=0.9
        )

    # --------------------------------
    # STEP 3: Build petals one by one
    # --------------------------------
    if frame >= 50:

        petals_to_show = min(
            petals,
            int((frame - 50) / 10) + 1
        )

        for p in range(petals_to_show):

            angle = 2 * np.pi * p / petals

            # Petal shape
            radius = 2.8 * V

            petal_x = radius * np.cos(U) * np.cos(angle)
            petal_y = radius * np.cos(U) * np.sin(angle)
            petal_z = 5 + radius * np.sin(U) * 0.45

            # Curve petals upward
            petal_z += 1.2 * V

            ax.plot_surface(
                petal_x,
                petal_y,
                petal_z,
                alpha=0.85,
                linewidth=0
            )

    # --------------------------------
    # STEP 4: Automatic 360° rotation
    # --------------------------------
    if frame > 110:

        rotation = (frame - 110) * 4

        ax.view_init(
            elev=25,
            azim=rotation
        )


# -----------------------------
# Start animation
# -----------------------------
animation = FuncAnimation(
    fig,
    update,
    frames=300,
    interval=80,
    repeat=True
)

plt.show()