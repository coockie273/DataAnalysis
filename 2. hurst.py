import pandas as pd
from hurst import compute_Hc

df = pd.read_csv("datasets/all_data.csv")

pid_to_filter = 'BK7610'
df = df[df['pid'] == pid_to_filter]

H, _, _ = compute_Hc(df['TAC_Reading'], min_window=100, max_window=100000, kind='price', simplified=True)
print(f"Hurst exponent: {H:.4f}")

df = pd.read_csv("BK7610_ema.csv")

H, _, _ = compute_Hc(df['EMA'], kind='price', min_window=100, max_window=100000, simplified=True)
print(f"Hurst exponent with smoothness: {H:.4f}")
