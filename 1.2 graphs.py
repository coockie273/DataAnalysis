import pandas as pd
import matplotlib.pyplot as plt


def union_data(pid_to_filter, column):
    data = pd.read_csv("datasets/all_data.csv")

    filtered_data = data[data['pid'] == pid_to_filter]
    filtered_data = filtered_data.iloc[125000:130000]

    filtered_data = filtered_data.sort_values(by='timestamp')

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data['timestamp'], filtered_data[column], linestyle='-', color='b')

    # Настройки графика
    plt.title(f"TAC Reading over Time for pid {pid_to_filter}")
    plt.xlabel('Timestamp')
    plt.ylabel('TAC Reading')
    plt.tight_layout()

    plt.show()


def tac_only(pid_to_filter):
    data = pd.read_csv(f"datasets/clean_tac/{pid_to_filter}_clean_TAC.csv")
    # filtered_data = filtered_data.iloc[::120]

    filtered_data = data.sort_values(by='timestamp')

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data['timestamp'], filtered_data['TAC_Reading'], linestyle='-', color='b')

    # Настройки графика
    plt.title(f"TAC Reading over Time for pid {pid_to_filter}")
    plt.xlabel('Timestamp')
    plt.ylabel('TAC Reading')
    plt.tight_layout()

    plt.show()


pid_to_filter = 'BK7610'

# tac_only(pid_to_filter)
union_data('BK7610', 'z')
