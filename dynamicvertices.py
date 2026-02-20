import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def create_dynamic_complete_graph(n):
    G = nx.complete_graph(n)
    # Initialize weights randomly
    for u, v in G.edges():
        G[u][v]['weight'] = round(random.uniform(1, 10), 2)
    return G

def update_weights(G):
    # Randomly update edge weights to simulate dynamic changes
    for u, v in G.edges():
        G[u][v]['weight'] = round(random.uniform(1, 10), 2)

def draw_graph(G, ax, pos):
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color='lightcoral', node_size=800, edge_color='gray', font_size=12, ax=ax)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    ax.set_title("Dynamic Moving Complete Graph with Changing Edge Weights")

def animate(i, G, ax, pos):
    update_weights(G)
    draw_graph(G, ax, pos)

def main():
    while True:
        try:
            n = int(input("Enter number of vertices (greater than 3): "))
            if n > 3:
                break
            else:
                print("Please enter a number greater than 3.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    G = create_dynamic_complete_graph(n)
    pos = nx.circular_layout(G)

    fig, ax = plt.subplots(figsize=(8,6))

    ani = animation.FuncAnimation(fig, animate, fargs=(G, ax, pos), interval=1500)

    plt.show()

if __name__ == "__main__":
    main()
