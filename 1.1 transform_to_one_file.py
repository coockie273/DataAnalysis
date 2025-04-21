import pandas as pd

accelerometer_data = pd.read_csv("datasets/all_accelerometer_data_pids_13.csv")

accelerometer_data['timestamp'] = (accelerometer_data['timestamp'] / 1000).astype(int)

phones = pd.read_csv("datasets/phone_types.csv")

ac_phones = pd.merge(accelerometer_data, phones, on='pid')

pids = pd.read_csv("datasets/pids.txt")

tac_data = pd.DataFrame()

all_data = pd.DataFrame()

for _, row in pids.iterrows():
    local_tac_data = pd.read_csv(f"datasets/clean_tac/{row['pid']}_clean_TAC.csv")

    ac_phones_sub = pd.merge(ac_phones[ac_phones['pid'] == row['pid']], local_tac_data, on='timestamp', how='left')
    ac_phones_sub = ac_phones_sub.sort_values(by='timestamp')

    ac_phones_sub.ffill(inplace=True)
    ac_phones_sub.bfill(inplace=True)

    all_data = pd.concat([all_data, ac_phones_sub], ignore_index=True)


all_data.to_csv("datasets/all_data.csv")
