import pandas as pd
from matplotlib import pyplot as plt
from nolitsa import delay, dimension
import numpy as np
from statsmodels.tsa.stattools import acf
from nolds import corr_dim


# Сигнал (временной ряд)
df = pd.read_csv("datasets/all_data.csv")

pid_to_filter = 'BK7610'
df = df[df['pid'] == pid_to_filter]
df = df.iloc[::120]

target = 'z'


def find_optimal_tau(ts, max_tau=10000):
    autocorr = acf(ts, nlags=max_tau)
    # Первый переход через ноль
    tau = np.argmin(autocorr[1:]) + 1
    return tau


def find_optimal_m_corr(ts, max_m=5, tau=1):
    d2_values = [corr_dim(ts, m, tau) for m in range(2, max_m + 1)]
    optimal_m = np.argmax(np.diff(d2_values) < 0.1) + 2
    return optimal_m, d2_values


def embed_time_series(time_series, tau, m):
    N = len(time_series)

    if N - (m - 1) * tau <= 0:
        raise ValueError("Размерность вложения или задержка слишком большие для данного временного ряда.")

    embedded = np.zeros((N - (m - 1) * tau, m))

    for t in range(N - (m - 1) * tau):
        for j in range(m):
            embedded[t, j] = time_series[t + j * tau]

    return embedded


tau = find_optimal_tau(df[target])
print(f"Оптимальная задержка (τ): {tau}")

m, d2 = find_optimal_m_corr(df[target], max_m=4, tau=tau)
print(f"Оптимальная m (CorrDim): {m}")

embedded_series = embed_time_series(np.array(df[target]), tau, m)
print("Вложенные векторы:")
print(embedded_series)

plt.figure(figsize=(10, 6))

# Для каждого вложенного вектора будем строить линию
for i in range(m):
    plt.plot(embedded_series[:, i], label=f"Признак {i+1}", marker='o')

plt.title("Вложенные векторы временного ряда")
plt.xlabel("Время")
plt.ylabel("Значения")
plt.legend()
plt.grid(True)
plt.show()
