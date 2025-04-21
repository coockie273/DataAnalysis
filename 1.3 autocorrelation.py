import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf


df = pd.read_csv("datasets/all_data.csv")

pid_to_filter = 'BK7610'

df = df[df['pid'] == pid_to_filter]

# Рассчитываем автокорреляцию для временного ряда (по колонке 'value')
lag_acf = acf(df['TAC_Reading'], nlags=1000000)

# Строим график автокорреляции
plt.figure(figsize=(10, 6))
plt.plot(range(len(lag_acf)), lag_acf, marker='o', color='b', label='ACF')
plt.title('Автокорреляция временного ряда')
plt.xlabel('Задержка (Lag)')
plt.ylabel('Корреляция')
plt.grid(True)
plt.legend()
plt.show()
