import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("project_data.csv")
close_col = df[['<CLOSE>']]


MA_close = []
kernel_size = 100
for i in range(0, (close_col.size - kernel_size + 1)):
    MA_close.append((np.sum(close_col[i:i+kernel_size]) / kernel_size))


plt.plot(close_col, label='main data')
plt.plot(MA_close, label='moving average')

plt.legend()
plt.show()