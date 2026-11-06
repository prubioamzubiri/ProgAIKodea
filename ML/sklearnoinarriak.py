import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split

df = pd.read_csv("etxeak.csv")

X = df[["azalera_m2", "gela_kopurua", "urte_eraikia"]]
y = df["prezioa"]

print(X.shape, y.shape)

modeloa = LinearRegression()

try:
    modeloa.fit(df[["azalera_m2"]],y)
except:
    print("zeozer gaizki joan da")

print(modeloa.predict([[90]])[0].round(2))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

modeloa2 = LinearRegression()

modeloa2.fit(X_train, y_train)

print(modeloa2.score(X_test, y_test))

print(modeloa2.coef_)
print(pd.Series(modeloa2.coef_, index=X.columns).round(1))
print(modeloa2.intercept_.round(2))

w0 = modeloa2.intercept_.round(2)
w1 =modeloa2.coef_[0].round(2)
w2 =modeloa2.coef_[1].round(2)
w3 =modeloa2.coef_[2].round(2)

print(f"Prezioa = {w0} + azalera(m2)*{w1} + gela_kopu * {w2} + urtea * {w3}")

print(modeloa2.predict(X_test.iloc[[0]]).round(2))

azalera_m2 = X_test.iloc[0]["azalera_m2"]
gela = X_test.iloc[0]["gela_kopurua"]
urtea = X_test.iloc[0]["urte_eraikia"]

predikzioa = w0 + azalera_m2*w1 + gela*w2 + urtea*w3
print(predikzioa.round(2))

import numpy as np 

rng2 = np.random.default_rng(1)
zarata = pd.DataFrame(rng2.normal(size=(len(X), 15)), columns=[f"z{i}" for i in
range(15)])
X_z = pd.concat([X.reset_index(drop=True), zarata], axis=1) # 3 benetako + 15
zarata
y_z = df["prezioa"] + rng2.normal(0, 50000, len(df)) # prezio zaratatsuagoak

Xz_tr, Xz_te, yz_tr, yz_te = train_test_split(X_z, y_z, train_size=0.25,random_state=0)

print(X_z)

from sklearn.preprocessing import StandardScaler

lr1 = LinearRegression()
lr2 = LinearRegression()

sc = StandardScaler()

A , B = sc.fit_transform(Xz_tr), sc.transform(Xz_te)

lr1.fit(X_z, y_z)
lr2.fit(A, yz_tr)

print(lr1.coef_)
print(lr2.coef_)


ridge = Ridge(alpha=3.0) #Modeloa sortu

ridge.fit(A,yz_tr) #Modeloa entrenatu (fit)

print(f"Ridge: {round(ridge.score(B,yz_te),2)}") #score / predict

lasso = Lasso(alpha=3000)

lasso.fit(A, yz_tr)

print(f"Lasso: {round(lasso.score(B,yz_te),2)}") #score / predict


#Ridge

print("alpha,   sc on Train,    sc on Test")
for alpha in [0.1, 1, 3, 10, 30, 100]:
    r = Ridge(alpha=alpha).fit(A, yz_tr)
    print(alpha, round(r.score(A, yz_tr), 3), round(r.score(B, yz_te), 3)
)

#Lasso
print("alpha,   sc on Train,    sc on Test,    W = 0")
for alpha in [100,1000,3000, 10000, 30000]:
    l = Lasso(alpha=alpha).fit(A, yz_tr)
    print(alpha, round(l.score(A, yz_tr), 3), round(l.score(B, yz_te), 3), sum(l.coef_==0))

print("")
l = Lasso(alpha=3000).fit(A, yz_tr)
print(l.coef_)

print("")
l = Lasso(alpha=10000).fit(A, yz_tr)
print(l.coef_)

print("")
l = Lasso(alpha=3000).fit(A, yz_tr)
print(l.coef_)

print("")
r = Ridge(alpha=3.0).fit(A, yz_tr)
print(r.coef_)

for i in range(5):
    Xz_tr, Xz_te, yz_tr, yz_te = train_test_split(X_z, y_z, train_size=0.25, random_state=i)
    sc = StandardScaler()
    Xz_tr_sc = sc.fit_transform(Xz_tr)
    Xz_te_sc = sc.transform(Xz_te)
    lasso = Lasso(alpha=3000)
    lasso.fit(Xz_tr_sc, yz_tr)
    print(f"{lasso.score(Xz_tr_sc, yz_tr)}      {lasso.score(Xz_te_sc, yz_te)}")


Xz_tr, Xz_te, yz_tr, yz_te = train_test_split(X_z, y_z, train_size=0.25, random_state=42)


print(f"media: {Xz_tr.mean(axis=0).round(2)}    debiazioa: {Xz_tr.std(axis=0).round(2)}")

sc = StandardScaler()
Xz_tr_sc = sc.fit_transform(Xz_tr)

print(f"media: {Xz_tr_sc.mean(axis=0).round(2)}    debiazioa: {Xz_tr_sc.std(axis=0).round(2)}")

Xz_te_sc = sc.transform(Xz_te)

print(f"media: {Xz_te_sc.mean(axis=0).round(2)}    debiazioa: {Xz_te_sc.std(axis=0).round(2)}")


from sklearn.preprocessing import MinMaxScaler

mm = MinMaxScaler()

print(f"media: {Xz_tr.mean(axis=0).round(2)}    debiazioa: {Xz_tr.std(axis=0).round(2)}")

Xz_tr_sc = mm.fit_transform(Xz_tr)

print(f"media: {Xz_tr_sc.mean(axis=0).round(2)}    debiazioa: {Xz_tr_sc.std(axis=0).round(2)}")

Xz_te_sc = mm.transform(Xz_te)

print(f"media: {Xz_te_sc.mean(axis=0).round(2)}    debiazioa: {Xz_te_sc.std(axis=0).round(2)}")

#####################ARIKETA##################################

df = pd.read_csv("etxeak.csv")

X = df[["azalera_m2", "prezioa", "urte_eraikia"]]
y = df["gela_kopurua"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)

from sklearn.neighbors import KNeighborsClassifier 


knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

print(f"normal: {knn.score(X_test, y_test)}")

mm = MinMaxScaler()

Xtr_sc = mm.fit_transform(X_train)
Xte_sc = mm.transform(X_test)


knnmm= KNeighborsClassifier(n_neighbors=5)

knnmm.fit(Xtr_sc, y_train)

print(f"MinMax: {knnmm.score(Xte_sc,y_test)}")

from sklearn.preprocessing import RobustScaler

mm = RobustScaler()

Xtr_sc = mm.fit_transform(X_train)
Xte_sc = mm.transform(X_test)


knnrs = KNeighborsClassifier(n_neighbors=5)

knnrs.fit(Xtr_sc, y_train)

print(f"RobustScaler: {knnrs.score(Xte_sc,y_test)}")

sc = StandardScaler()

Xtr_sc = sc.fit_transform(X_train)
Xte_sc = sc.transform(X_test)

knnsc = KNeighborsClassifier(n_neighbors=5)

knnsc.fit(Xtr_sc, y_train)

print(f"StandardScaler: {knnsc.score(Xte_sc,y_test)}")




prezioa = int(input("Prezioa eman: "))
urtea = int(input("Eraikitako urtea eman: "))
m2 = int(input("Azalera eman: "))

X_berria = pd.DataFrame([[m2, prezioa, urtea]], columns=["azalera_m2", "prezioa", "urte_eraikia"])

X_berria_sc = sc.transform(X_berria)

print("gela kopurua: ", knnsc.predict(X_berria_sc))
















prezioa = int(input("Prezioa eman: "))
urtea = int(input("Eraikitako urtea eman: "))
m2 = int(input("Azalera eman: "))

X_berria = pd.DataFrame([[m2, prezioa, urtea]], columns=["azalera_m2", "prezioa", "urte_eraikia"])

print("gela kopurua: ", knn.predict(X_berria)[0])
