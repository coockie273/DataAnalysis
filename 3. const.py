import pandas as pd
from nolitsa import delay, dimension
import numpy as np

# Сигнал (временной ряд)
df = pd.read_csv("datasets/all_data.csv")

pid_to_filter = 'BK7610'
df = df[df['pid'] == pid_to_filter]

# Найдём оптимальную задержку (τ)
mi = delay.mi(df['TAC_Reading'])  # mutual information
tau_opt = np.argmin(mi)
print(f'Оптимальная задержка (τ): {tau_opt}')

# Найдём размерность вложения (m)
m_fnn = dimension.fnn(df['TAC_Reading'], tau=tau_opt, dim=10)
m_opt = np.argmax(float(m_fnn) < 0.01)  # когда ложных соседей < 1%

print(f'Оптимальная размерность вложения (m): {m_opt}')