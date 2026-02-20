import matplotlib
matplotlib.use("TkAgg")   # Ensures interactive window in VS Code

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Create figure
fig, ax = plt.subplots()

data = []

def update(frame):
    ax.clear()   # Clear previous histogram
    
    # Add new random value
    data.append(random.randint(1, 100))
    
    # Plot updated histogram
    ax.hist(data, bins=10, color='skyblue', edgecolor='black')
    
    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")

# Animate
ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()