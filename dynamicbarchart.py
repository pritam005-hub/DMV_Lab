import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

categories = ['A', 'B', 'C', 'D', 'E']
values = np.array([4, 7, 3, 8, 5], dtype=float)

fig, ax = plt.subplots()
ax.set_ylim(0, 10)
ax.set_title("Dynamic Animated Bar Chart")

bars = ax.bar(categories, values, color='orange')

def animate(frame):
    global values
    # Random fluctuation
    values += (np.random.rand(len(values)) - 0.5)
    values = np.clip(values, 0, 10)
    
    for bar, val in zip(bars, values):
        bar.set_height(val)
    return bars

ani = animation.FuncAnimation(fig, animate, frames=200, interval=100, blit=False)
plt.show()
