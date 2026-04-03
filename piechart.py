import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Pritam_DMV_Daatset.csv")

x = df.iloc[:5, 0]   # first 5 values (for clarity)
y = df.iloc[:5, 1]

plt.figure()
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()