from sklearn.datasets import load_iris

df_iris = load_iris(as_frame=True)

X = df_iris.data
y = df_iris.target

print(X.shape)
print(y.shape)

print(list(X.columns))
print(df_iris.target_names)

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.8, random_state=42)

eredua = KNeighborsClassifier(n_neighbors=3)
eredua.fit(X_train, y_train)

berria = X.iloc[[100]] # lore bat, adibide gisa
print(berria)

print(eredua.predict(berria))
print(df_iris.target_names)

print(df_iris.target_names[eredua.predict(berria)])

print(eredua.score(X_test, y_test))

from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)

X = wine.data
y = wine.target

print(X.shape)
print(X.describe())

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42)

eredua = KNeighborsClassifier(n_neighbors=3)
eredua.fit(X_train, y_train)

print(eredua.score(X_test, y_test))