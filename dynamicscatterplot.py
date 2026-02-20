import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Initial random data
np.random.seed(2)
num_points = 30
x = np.random.rand(num_points)
y = np.random.rand(num_points)

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Dynamic Animated Scatter Plot")

scat = ax.scatter(x, y, c='red')

def animate(frame):
    # Move points randomly
    global x, y
    x += (np.random.rand(num_points) - 0.5) * 0.05
    y += (np.random.rand(num_points) - 0.5) * 0.05
    
    # Keep inside bounds
    x = np.clip(x, 0, 1)
    y = np.clip(y, 0, 1)

    scat.set_offsets(np.column_stack((x, y)))
    return scat,

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=200,
    interval=100,
    blit=True
)

plt.show()
