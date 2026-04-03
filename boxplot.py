import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Pritam_DMV_Daatset.csv")

y = df.iloc[:, 1]

plt.figure()
plt.boxplot(y)
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()