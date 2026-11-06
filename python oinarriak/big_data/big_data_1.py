import pandas as pd

datuak = {
 "izena": ["Ane", "Jon", "Uxue", "Iker", "Pablo"],
 "adina": [16, 17, 16, 18, 24],
 "nota": [7, 8, 5, 9, 2]
 }

dataframea = pd.DataFrame(datuak)

print(dataframea.head(2))
print(dataframea.describe())
print(dataframea.info())

print(dataframea)

dataframea.to_csv("emaitza.csv", index=False)

dataframe2 = pd.read_csv("emaitza.csv")

print("")
print(dataframe2)


suspenditu_duten_izenak = dataframea[dataframea["nota"] < 5]["izena"]
#suspenditu_duten_izenak = df[df["nota"] < 5]["izena"]

print(dataframea[dataframea["adina"] >= 17 ])
print(dataframea[dataframea["nota"] < 5]["izena"])
print(dataframea[(dataframea["adina"] == 16) & (dataframea["nota"] >=5)])


dataframea["gaindituak"] = dataframea["nota"] >= 7
dataframea["nota_100"] = dataframea["nota"] * 10
print(dataframea)

dataframea.to_csv("emaitza.csv", index=False)