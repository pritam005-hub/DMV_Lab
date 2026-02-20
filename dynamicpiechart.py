import matplotlib
matplotlib.use("TkAgg")  # For VS Code interactive window

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()

labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 30, 20, 25]

def update(frame):
    ax.clear()
    # Update sizes with random values
    new_sizes = [random.randint(10, 40) for _ in labels]
    
    ax.pie(new_sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title("Dynamic Pie Chart (Updating)")

ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()