# static_complete_graph.py

import networkx as nx
import matplotlib.pyplot as plt

# Create a static complete graph
def create_static_complete_graph(n):
    G = nx.complete_graph(n)
    return G

# Display graph data
def graph_data_management(G):
    print("\n--- Graph Data Management ---")
    print("Vertices:", list(G.nodes))
    print("Edges:", list(G.edges))
    print("Number of vertices:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())

# Visualize the graph
def visualize_graph(G):
    pos = nx.circular_layout(G)
    plt.figure(figsize=(8,6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, edge_color='gray', font_size=12)
    plt.title("Static Complete Graph")
    plt.show()

# Main function
def main():
    while True:
        try:
            n = int(input("Enter the number of vertices (greater than 3): "))
            if n > 3:
                break
            else:
                print("Please enter a number greater than 3.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    G = create_static_complete_graph(n)
    graph_data_management(G)
    visualize_graph(G)

if __name__ == "__main__":
    main()