import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

fig, ax = plt.subplots()
ax.set_title("3D-Style Rotating Pie Chart")

def animate(frame):
    ax.clear()
    ax.set_title("3D-Style Rotating Pie Chart")

    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=frame * 3,
        colors=colors,
        shadow=True,
        wedgeprops=dict(width=0.5)  # Donut style
    )

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=360,
    interval=30,
    repeat=True
)

plt.show()
