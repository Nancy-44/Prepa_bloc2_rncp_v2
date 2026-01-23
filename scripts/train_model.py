import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("/home/ubuntu/Bloc2_v2/data/users_clean_csv.csv")

# Target
df["account_status"] = df["account_status"].map({
    "inactive": 0,
    "active": 1
})
# feautures numériques uniquement
features = ["age", "monthly_spend"]
X = df[features]
#X = df.drop(columns=["monthly_spend"])
y = df["account_status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LinearRegression()
model = LogisticRegression() 
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Model accuracy:", round(accuracy_score(y_test, y_pred), 2))

joblib.dump(model, "/home/ubuntu/Bloc2_v2/models/monthly_spend_model.joblib")