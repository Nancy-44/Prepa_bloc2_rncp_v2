import pandas as pd

def test_no_duplicates():
    df = pd.read_csv("/home/ubuntu/Bloc2_v2/data/users_clean_csv.csv")
    assert df.duplicated().sum() == 0

def test_required_columns():
    df = pd.read_csv("/home/ubuntu/Bloc2_v2/data/users_clean_csv.csv")
    for col in ["id", "gender", "age"]:
        assert col in df.columns