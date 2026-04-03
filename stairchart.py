import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Pritam_DMV_Daatset.csv")

x = df.iloc[:, 0]
y = df.iloc[:, 1]

plt.figure()
plt.step(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Step Chart")
plt.xticks(rotation=45)
plt.show()