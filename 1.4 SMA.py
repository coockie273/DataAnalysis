import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/all_data.csv")

pid_to_filter = 'BK7610'
df = df[df['pid'] == pid_to_filter]

# Вычисление скользящего среднего с окном 10
df['SMA'] = df['TAC_Reading'].rolling(window=100000).mean()

df.to_csv('BK7610_sma.csv')

# df['sma_shifted_left'] = df['SMA'].shift(-50000)

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(df['TAC_Reading'], label='Original Data')
plt.plot(df['SMA'], label='Smoothed Data (SMA)')
# plt.plot(df['sma_shifted_left'], label='Smoothed Data (SMA)')
plt.title('Скользящее Среднее (SMA)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
