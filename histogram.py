import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Pritam_DMV_Daatset.csv")

y = df.iloc[:, 1]

plt.figure()
plt.hist(y, bins=10)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()