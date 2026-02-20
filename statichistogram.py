import matplotlib.pyplot as plt

# Sample data
data = [12, 15, 18, 20, 22, 25, 30, 35, 40, 45, 50, 18, 22, 25]

# Create histogram
plt.hist(data, bins=5, color='skyblue', edgecolor='black')

plt.title("Static Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()