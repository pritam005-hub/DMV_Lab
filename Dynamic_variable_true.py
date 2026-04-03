import matplotlib.pyplot as plt

# Ask user for input
x = input("Enter X values separated by commas: ").split(',')
y = input("Enter Y values separated by commas: ").split(',')

# Convert input strings to floats
x = [float(i) for i in x]
y = [float(i) for i in y]

# Plot the data
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Add labels and title
plt.xlabel("X values (Independent Variable)")
plt.ylabel("Y values (Dependent Variable)")
plt.title("Dynamic X-Y Plot")

# Show grid
plt.grid(True)

# Display plot
plt.show()