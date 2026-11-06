import pandas as pd

df = pd.read_csv("emaitza.csv")

print(df.isna())
print(df.isna().sum())
print(df.dropna())
print(df.fillna(0))

df["gaindituak"] = df["gaindituak"].fillna(df["nota"] >= 7)
print(df)

df["nota"] = df["nota"].fillna(df["nota"].mean())
print(df)

