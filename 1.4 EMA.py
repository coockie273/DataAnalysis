import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def ema(column, pid_to_filter):

    df = pd.read_csv("datasets/all_data.csv")

    pid_to_filter = 'BK7610'
    df = df[df['pid'] == pid_to_filter]

    df = df.iloc[128500:129500]

    df['EMA'] = df[column].ewm(span=10, adjust=False).mean()

    df.to_csv('BK7610_ema.csv')

    # Построение графиков
    plt.figure(figsize=(10, 6))
    plt.plot(df[column], label='Original Data')
    plt.plot(df['EMA'], label='Smoothed Data (EMA)')
    plt.title('Экспоненциальное Сглаживание (EMA)')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()


def ema_tac_only(pid_to_filter):

    data = pd.read_csv(f"datasets/clean_tac/{pid_to_filter}_clean_TAC.csv")

    data['EMA'] = data['TAC_Reading'].ewm(span=10, adjust=False).mean()

    data.to_csv('BK7610_ema.csv')

    # Построение графиков
    plt.figure(figsize=(10, 6))
    plt.plot(data['TAC_Reading'], label='Original Data')
    plt.plot(data['EMA'], label='Smoothed Data (EMA)')
    plt.title('Экспоненциальное Сглаживание (EMA)')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()


pid_to_filter = 'BK7610'

ema_tac_only(pid_to_filter)

# ema('x', pid_to_filter)
# ema('y', pid_to_filter)
# ema('z', pid_to_filter)


