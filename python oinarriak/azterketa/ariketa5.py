import pandas as pd

df = pd.read_csv("eguraldia.csv")

print(f"Tenperatura mx {df["tenperatura"].max()}")
print(f"Tenperatura mn {df["tenperatura"].min()}")
print(f"Tenperatura batazbestekoa {df["euria_mm"].mean()}")

egun_kopurua = 0

for i in range(len(df)):

    if df.iloc[i]["tenperatura"] > 20 and df.iloc[i]["euria_mm"] > 10:
        egun_kopurua += 1


print(egun_kopurua)