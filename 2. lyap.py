import nolds
import pandas as pd

df = pd.read_csv("datasets/all_data.csv")

pid_to_filter = 'BK7610'
df = df[df['pid'] == pid_to_filter]

df = df.iloc[::120]

series = df['TAC_Reading']

lyap_r = nolds.lyap_r(series, min_tsep=20)
print("Ляпуновская экспонента (Вольф):", lyap_r)
