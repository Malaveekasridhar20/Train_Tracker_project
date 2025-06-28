import pandas as pd

def get_train_status_offline(train_no):
    try:
        df = pd.read_csv("data/train_status_data.csv")
        row = df[df['train_no'] == int(train_no)].iloc[0]
        return {
            "status": row['status'],
            "location": row['location'],
            "eta": row['eta']
        }
    except:
        return None
