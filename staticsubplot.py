import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# First subplot
axs[0].plot(x, y1, color='blue', label='sin(x)')
axs[0].set_title('Sine Wave')
axs[0].legend()
axs[0].grid(True)

# Second subplot
axs[1].plot(x, y2, color='red', label='cos(x)')
axs[1].set_title('Cosine Wave')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
