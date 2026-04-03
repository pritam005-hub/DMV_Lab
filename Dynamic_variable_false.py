import matplotlib.pyplot as plt


x = input("Enter X values separated by commas: ").split(',')
y = input("Enter Y values separated by commas: ").split(',')


x = [float(i) for i in x]
y = [float(i) for i in y]


plt.plot(x, y, marker='o', linestyle='-', color='blue')


plt.xlabel("X values (Independent Variable)")
plt.ylabel("Y values (Dependent Variable)")
plt.title("Dynamic X-Y Plot")


plt.grid(False)


plt.show()