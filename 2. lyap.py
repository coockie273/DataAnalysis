import nolds
import pandas as pd

df = pd.read_csv("datasets/all_data.csv")

pid_to_filter = 'BK7610'
df = df[df['pid'] == pid_to_filter]

df = df.iloc[0:10000]

series = df['TAC_Reading'].dropna().astype(float).values
print("Длина ряда:", len(series))

if len(series) < 100:
    raise ValueError("Слишком мало данных для анализа!")

lyap_e = nolds.lyap_r(series, emb_dim=5, matrix_dim=3)
print("Ляпуновская экспонента (Вольф):", lyap_e)
