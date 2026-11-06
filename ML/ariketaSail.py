from sklearn.datasets import load_breast_cancer

data = load_breast_cancer(as_frame=True)

from sklearn.model_selection import train_test_split

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2, stratify=y)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=11)
knn.fit(X_train_sc, y_train)

from sklearn.metrics import classification_report

y_pred = knn.predict(X_test_sc)

print(classification_report(y_test,y_pred))

print(knn.score(X_test_sc, y_test))
#-----------------------------------------------------------------

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=11)
tree.fit(X_train_sc, y_train)

y_pred = tree.predict(X_test_sc)

print(classification_report(y_test,y_pred))

print(tree.score(X_test_sc, y_test))

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X_train_sc, y_train)

y_pred = lr.predict(X_test_sc)

print(classification_report(y_test,y_pred))

print(lr.score(X_test_sc, y_test))