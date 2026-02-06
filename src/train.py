import pandas as pd
import pickle

from xgboost import XGBClassifier


def load_data():

    df = pd.read_csv('../data/creditcard.csv')
    df = df.drop_duplicates().reset_index(drop=True)

    df.columns = df.columns.str.lower()
    df = df.rename(columns={"class": "fraud"})
    
    del df['time']

    print('Data was loaded successfully')
    return df


def train_model(df):
    
    features = df.drop(columns="fraud").columns.to_list()
    y = df['fraud'].values
    
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

    xgb.fit(df[features],y)

    print('Model was trained successfully')

    return xgb

def save_model(filename, model):
    with open(filename, 'wb') as f_out:
        pickle.dump(model, f_out)
    
    print('Model saved to', filename)

def main():
    df = load_data()
    model = train_model(df)
    save_model('model.bin', model)

if __name__ == "__main__":
    main()