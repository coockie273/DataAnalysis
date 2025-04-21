import pandas as pd


def metrics(df, field):

    print(f"Среднее значение {field}: {df[field].mean()}")
    print(f"Медиана {field}: {df[field].median()}")
    print(f"Стандартное отклонение {field}: {df[field].var()}")
    print(f"Минимум {field}: {df[field].min()}")
    print(f"Максимум {field}: {df[field].max()}")


data = pd.read_csv("datasets/all_data.csv")

metrics(data, 'TAC_Reading')
metrics(data, 'x')
metrics(data, 'y')
metrics(data, 'z')
