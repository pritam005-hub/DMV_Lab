import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Data
x = np.linspace(0, 2 * np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

line1, = axs[0].plot([], [], color='blue', label='sin(x)')
line2, = axs[1].plot([], [], color='red', label='cos(x)')

axs[0].set_xlim(0, 2*np.pi)
axs[0].set_ylim(-1.5, 1.5)
axs[0].set_title('Sine Wave')
axs[0].grid(True)

axs[1].set_xlim(0, 2*np.pi)
axs[1].set_ylim(-1.5, 1.5)
axs[1].set_title('Cosine Wave')
axs[1].grid(True)

# Initialization function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Animation function
def animate(i):
    line1.set_data(x[:i], y1[:i])
    line2.set_data(x[:i], y2[:i])
    return line1, line2

# Animate
ani = FuncAnimation(fig, animate, frames=len(x), init_func=init, blit=True, interval=20)

plt.tight_layout()
plt.show()
