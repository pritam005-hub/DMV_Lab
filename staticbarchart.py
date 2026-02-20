import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 7, 3, 8, 5]

fig, ax = plt.subplots()
ax.set_ylim(0, 10)
ax.set_title("Static Bar Chart")

bars = ax.bar(categories, [0]*len(values), color='skyblue')

def animate(frame):
    progress = min(frame/30, 1)
    for bar, val in zip(bars, values):
        bar.set_height(val * progress)
    return bars

ani = animation.FuncAnimation(fig, animate, frames=31, interval=100, blit=False, repeat=False)
plt.show()
