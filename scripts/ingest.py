import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/mydatabase")

df = pd.read_csv("/home/ubuntu/Bloc2_v2/data/users_clean_csv.csv")
df.to_sql("users", engine, if_exists="append", index=False)