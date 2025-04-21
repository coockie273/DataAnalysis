import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/all_data.csv")

pid_to_filter = 'BK7610'
df = df[df['pid'] == pid_to_filter]

df['EMA'] = df['TAC_Reading'].ewm(span=10000, adjust=False).mean()

df.to_csv('BK7610_ema.csv')

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(df['TAC_Reading'], label='Original Data')
plt.plot(df['EMA'], label='Smoothed Data (EMA)')
plt.title('Экспоненциальное Сглаживание (EMA)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
