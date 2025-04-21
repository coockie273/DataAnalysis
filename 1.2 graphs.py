import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("datasets/all_data.csv")

pid_to_filter = 'BK7610'
filtered_data = data[data['pid'] == pid_to_filter]

filtered_data = filtered_data.sort_values(by='timestamp')

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['timestamp'], filtered_data['TAC_Reading'], marker='o', linestyle='-', color='b')

# Настройки графика
plt.title(f"TAC Reading over Time for pid {pid_to_filter}")
plt.xlabel('Timestamp')
plt.ylabel('TAC Reading')
plt.tight_layout()

# Показать график
plt.show()
