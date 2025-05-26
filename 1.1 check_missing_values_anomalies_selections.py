import numpy as np
import pandas as pd


def IQR(df, field, window_size):

    rolling_median = df[field].rolling(window=window_size).median()
    rolling_iqr = df[field].rolling(window=window_size).apply(
        lambda x: np.percentile(x, 75) - np.percentile(x, 25))

    outliers = df[abs(df[field] - rolling_median) > 1.5 * rolling_iqr]

    print(f"Выбросы для поля {field}:")
    print(outliers)


df = pd.read_csv("datasets/all_data.csv")

missing_values_columns = df.isna().sum()

total_missing_values = df.isna().sum().sum()

print("Количество пропущенных значений по столбцам:")
print(missing_values_columns)

print("\nОбщее количество пропущенных значений:")
print(total_missing_values)

IQR(df, "TAC_Reading", 100000)
IQR(df, "x", 100000)
IQR(df, "y", 100000)
IQR(df, "z", 100000)

