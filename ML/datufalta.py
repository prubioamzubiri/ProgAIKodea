import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

etxeak = pd.read_csv("etxeak.csv")

X = etxeak[["azalera_m2","gela_kopurua", "urte_eraikia"]]
y = etxeak ["prezioa"]

Xn = X.astype(float)
r2 = np.random.default_rng(7)
Xn.loc[r2.choice(len(Xn), 8, replace=False), "azalera_m2"] = np.nan
Xn.loc[r2.choice(len(Xn), 6, replace=False), "urte_eraikia"] = np.nan
print(Xn.isna().sum().to_dict()) 

print(Xn)

a, b, c, d = train_test_split(Xn, y, test_size=0.2, random_state=42)
try:
    LinearRegression().fit(a, c)
except ValueError as e:
    print(str(e).split(".")[0]) # Input X contains NaN




df = pd.read_csv("etxeak.csv")

X = df[["azalera_m2"]]
y = df["prezioa"]

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree=2, include_bias=False)
X_tr_p = pf.fit_transform(X_tr)
X_te_p = pf.transform(X_te)

print(pf.get_feature_names_out())

eredua_pol = LinearRegression().fit(X_tr_p, y_tr)
print(eredua_pol.score(X_te_p, y_te)) # 0.988

X = etxeak[["azalera_m2","gela_kopurua", "urte_eraikia"]]

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

pf = PolynomialFeatures(degree=12)
X_tr_p = pf.fit_transform(X_tr)
X_te_p = pf.transform(X_te)

print(pf.get_feature_names_out())

eredua_pol = LinearRegression().fit(X_tr_p, y_tr)
print(eredua_pol.score(X_te_p, y_te)) # 0.988


import matplotlib.pyplot as plt 


f = lambda x: x**5 + 4*x**4 - 3*x**3 + x + 4
x = np.linspace(-1,1,500)
plt.plot(x,f(x))
plt.show()

X = df[["azalera_m2"]]
y = df["prezioa"]

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

for i in range(5):
    pf = PolynomialFeatures(degree=i+2, include_bias=False)
    X_tr_p = pf.fit_transform(X_tr)

    azalerak = np.linspace(20,120,10)
    azalerak = azalerak.reshape(-1, 1)
    X_froga = pf.transform(azalerak)

    eredua_pol = LinearRegression().fit(X_tr_p, y_tr)

    plt.plot(azalerak.ravel(), eredua_pol.predict(X_froga))
    plt.show()

