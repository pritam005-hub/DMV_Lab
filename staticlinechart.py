import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 140, 180, 200]

# Create line chart
plt.plot(months, sales, marker='o', linestyle='-', color='blue')

# Add title and labels
plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales")

# Show grid
plt.grid(True)

# Display the chart
plt.show()