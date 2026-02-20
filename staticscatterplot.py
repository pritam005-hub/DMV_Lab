import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Data
np.random.seed(1)
x = np.random.rand(30)
y = np.random.rand(30)

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Static Scatter Plot")

scat = ax.scatter([], [])

def animate(frame):
    scat.set_offsets(np.column_stack((x[:frame], y[:frame])))
    return scat,

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=len(x) + 1,
    interval=200,
    blit=True,
    repeat=False
)

plt.show()
