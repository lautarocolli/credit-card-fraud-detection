import pandas as pd
import pickle

from xgboost import XGBClassifier


def load_data():

    df = pd.read_csv('../data/creditcard.csv')
    df = df.drop_duplicates().reset_index(drop=True)

    df.columns = df.columns.str.lower()
    df = df.rename(columns={"class": "fraud"})

    y = df['fraud'].values

    del df['time']
    del df['fraud']

    print('Data has loaded successfully')
    return df,y


def train_model(df,y):
    xgb = XGBClassifier(
        n_estimators = 100,
        learning_rate = 0.05,

        colsample_bytree = 0.8,
        gamma = 0,
        max_depth = 6,
        min_child_weight = 1,
        subsample = 0.8,

        objective="binary:logistic",
        eval_metric="aucpr",
        
        random_state=1,
        n_jobs=-1
    )

    xgb.fit(df,y)

    print('Model has trained successfully')

    return xgb

def save_model(filename, model):
    with open(filename, 'wb') as f_out:
        pickle.dump(model, f_out)
    
    print('Model saved to', filename)

def main():
    df, y = load_data()
    model = train_model(df, y)
    save_model('model.bin', model)

if __name__ == "__main__":
    main()