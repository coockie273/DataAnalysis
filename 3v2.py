import numpy as np
from gtda import time_series
import pandas as pd
from matplotlib import pyplot as plt


def embed_time_series(time_series, tau, m):
    N = len(time_series)

    if N - (m - 1) * tau <= 0:
        raise ValueError("Размерность вложения или задержка слишком большие для данного временного ряда.")

    embedded = np.zeros((N - (m - 1) * tau, m))

    for t in range(N - (m - 1) * tau):
        for j in range(m):
            embedded[t, j] = time_series[t + j * tau]

    return embedded


df = pd.read_csv("datasets/all_data.csv")

pid_to_filter = 'BK7610'
df = df[df['pid'] == pid_to_filter]
df = df.iloc[::120]

tau_x, m_x = time_series.takens_embedding_optimal_parameters(df['x'], 10000, 10)

print(f"Оптимальная задержка x (τ): {tau_x}")
print(f"Оптимальная x m: {m_x}")

embedded_series_x = embed_time_series(np.array(df['x']), tau_x, m_x)
print("Вложенные x векторы:")
print(embedded_series_x)

tau_y, m_y = time_series.takens_embedding_optimal_parameters(df['y'], 10000, 10)

print(f"Оптимальная задержка y (τ): {tau_y}")
print(f"Оптимальная y m: {m_y}")

embedded_series_y = embed_time_series(np.array(df['y']), tau_y, m_y)
print("Вложенные векторы:")
print(embedded_series_y)

tau_z, m_z = time_series.takens_embedding_optimal_parameters(df['z'], 10000, 10)

print(f"Оптимальная задержка y (τ): {tau_z}")
print(f"Оптимальная y m: {m_z}")

embedded_series_z = embed_time_series(np.array(df['z']), tau_z, m_z)
print("Вложенные векторы:")
print(embedded_series_z)

# plt.figure(figsize=(10, 6))
#
# # Для каждого вложенного вектора будем строить линию
# for i in range(m):
#     plt.plot(embedded_series[:, i], label=f"Признак {i+1}", marker='o')
#
# plt.title("Вложенные векторы временного ряда")
# plt.xlabel("Время")
# plt.ylabel("Значения")
# plt.legend()
# plt.grid(True)
# plt.show()


def phase_portrait(series, tau, m, title):
    n = len(series)
    embedded = np.zeros((n - (m - 1) * tau, m))

    for i in range(m):
        embedded[:, i] = series[i * tau: n - (m - 1 - i) * tau]

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(embedded[:, 0], embedded[:, 1], embedded[:, 2], lw=0.5)
    ax.set_title(f"Фазовый портрет ({title}), τ={tau}, m={m}")
    ax.set_xlabel("X(t)")
    ax.set_ylabel(f"X(t + {tau})")
    ax.set_zlabel(f"X(t + {2 * tau})")
    plt.show()


# Построение для каждого ряда
phase_portrait(df['x'], tau_x, m_x, "X-ряд")
phase_portrait(df['y'], tau_y, m_y, "Y-ряд")
phase_portrait(df['z'], tau_z, m_z, "Z-ряд")

