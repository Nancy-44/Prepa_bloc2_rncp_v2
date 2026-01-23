import pandas as pd
from psutil import users

def extract():
    users_csv = pd.read_csv("/home/ubuntu/Bloc2_v2/data/users.csv")
    users_json = pd.read_json("/home/ubuntu/Bloc2_v2/data/users.json")
    return users_csv, users_json

def transform(users_csv):
    users_csv['age'].fillna(users_csv['age'].median(), inplace=True)  # Exemple de remplissage des valeurs manquantes avec la médiane
    users_csv['monthly_spend'].fillna(users_csv['monthly_spend'].mean(), inplace=True)  # Exemple de remplissage des valeurs manquantes avec la moyenne
    users_csv['gender'] = users_csv['gender'].fillna('Unknown')
    users_csv['email'] = users_csv['email'].fillna('unknown@mail.com')
    users_csv['account_status'] = users_csv['account_status'].fillna('inactive')
    users_csv["signup_date"] = pd.to_datetime(users_csv["signup_date"], errors='coerce')
    users_csv["last_login"] = pd.to_datetime(users_csv["last_login"], errors='coerce')
    users_csv['signup_date'] = users_csv['signup_date'].fillna(users_csv['signup_date'].median())
    users_csv['last_login'] = users_csv['last_login'].fillna(users_csv['last_login'].median())
    users_csv.loc[users_csv["age"] > 100, "age"] = users_csv["age"].quantile(0.75)
    users_csv["age"] = users_csv["age"].astype(int)
    users_csv = users_csv.drop_duplicates()
    return users_csv

def load(df):
    df.to_csv("/home/ubuntu/Bloc2_v2/data/users_clean_csv.csv", index=False)

if __name__ == "__main__":
    users_csv, users_json = extract()
    users_clean_csv = transform(users_csv)
    load(users_clean_csv)