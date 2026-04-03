import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Pritam_DMV_Daatset.csv")

x = df.iloc[:, 0]
y = df.iloc[:, 1]

plt.figure()
plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Chart")
plt.xticks(rotation=45)
plt.show()