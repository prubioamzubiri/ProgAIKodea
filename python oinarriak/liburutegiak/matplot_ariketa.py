import pandas as pd
import matplotlib.pyplot as plt

k_p = pd.read_csv("CSV/precios_consolas.csv")

precio_PC = k_p["PC"].mean()
consolas = ["Xbox", "PS5", "Switch", "PC"]
preciomedio =[k_p[x].mean() for x in consolas]

plt.bar(consolas,preciomedio)
plt.show()

count_price = [0,0]

for x in range(len(k_p)):
    if k_p.iloc[x]["PC"] > k_p[["PS5", "Switch","Xbox"]].iloc[x].max():
        count_price[0] += 1
    else:
        count_price[1] += 1

X2 = ["PC más caro", "PC no mas caro"]
plt.bar(X2,count_price)
plt.show()


count_price_c = [0,0,0]

precios_con = k_p[["PS5", "Xbox", "Switch"]]

for i in range(len(k_p)):

    minimo = precios_con.iloc[i].min()

    if minimo == k_p.iloc[i]["PS5"]:
        count_price_c[0] += 1
    elif minimo == k_p.iloc[i]["Xbox"]:
        count_price_c[1] += 1
    else:
        count_price_c[2] += 1

X3 = ["PS5", "Xbox", "Switch"]
plt.bar(X3,count_price_c)
plt.show()