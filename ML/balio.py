import numpy as np, pandas as pd
rng = np.random.default_rng(1)
n = 400
ordu = rng.uniform(0, 12, n).round(1)
asist = rng.uniform(40, 100, n).round()
nota = rng.uniform(0, 10, n).round(1)
lanean = rng.choice(["ez", "partziala", "osoa"], n)
efektua = pd.Series(lanean).map({"ez": 0, "partziala": 0.5, "osoa": 1.2}).to_numpy()
logit = 1.6 * (1.4 - 0.45*ordu - 0.06*(asist-70) - 0.3*(nota-5) + efektua)
arriskuan = rng.uniform(size=n) < 1 / (1 + np.exp(-logit))

df = pd.DataFrame({"ordu_ikasketa": ordu, "asistentzia": asist,
"aurreko_nota": nota, "lanean": lanean,
"arriskuan": arriskuan.astype(int)})
df.loc[rng.choice(n, 20, replace=False), "aurreko_nota"] = np.nan
print(df.isna().sum().to_dict())

from sklearn.model_selection import train_test_split

X = df.drop(columns="arriskuan")
y = df["arriskuan"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

from sklearn.linear_model import LogisticRegression

Xn = df[["ordu_ikasketa", "asistentzia"]]
emaitzak = []

for rs in range(10):
    Xa, Xb, ya, yb = train_test_split(Xn, y, test_size=0.25,random_state=rs, stratify=y)
    emaitzak.append(LogisticRegression().fit(Xa, ya).score(Xb, yb))

print(min(emaitzak), max(emaitzak)) # 0.76 0.84

from sklearn.model_selection import cross_validate, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier

kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
emaitzatree = cross_validate(DecisionTreeClassifier(max_depth=3), Xn, y, cv=kf,
                       scoring=["accuracy", "precision", "recall", "f1"])

print(pd.DataFrame(emaitzatree).mean().round(3))


emaitzalr = cross_validate(LogisticRegression(), Xn, y, cv=kf,
                       scoring=["accuracy", "precision", "recall", "f1"])

print(pd.DataFrame(emaitzalr).mean().round(3))

from sklearn.neighbors import KNeighborsClassifier

emaitzaknn = cross_validate(KNeighborsClassifier(n_neighbors=11), Xn, y, cv=kf,
                       scoring=["accuracy", "precision", "recall", "f1"])

print(pd.DataFrame(emaitzaknn).mean().round(3))


from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

lehen_pipe = make_pipeline(StandardScaler(), LogisticRegression())
emaitzak = cross_validate(lehen_pipe, Xn, y, cv=kf, scoring=["accuracy", "precision", "recall", "f1"])
print(pd.DataFrame(emaitzak).mean().round(3))


from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

num = ["ordu_ikasketa", "asistentzia", "aurreko_nota"]
kat = ["lanean"]

preprod = ColumnTransformer([
    ("numerikoa", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), num),
    ("Kategoria", OneHotEncoder(), kat)
])

lehen_pipeline = Pipeline([
    ("aurreprozesamendua", preprod),
    ("klasifikadorea", LogisticRegression())
])

lehen_pipeline.fit(X_train, y_train)
print(lehen_pipeline.score(X_test, y_test))

print(list(lehen_pipeline.named_steps))

print(lehen_pipeline.predict(X_test))
print(lehen_pipeline.predict_proba(X_test))

from sklearn.model_selection import GridSearchCV

param_grid = {"klasifikadorea__C": [0.01, 0.1, 1, 10, 100]}
bilaketa = GridSearchCV(lehen_pipeline, param_grid, cv=5, scoring="f1")
bilaketa.fit(X_train, y_train)
print(bilaketa.best_params_) # {'clf__C': 1}
print(round(bilaketa.best_score_, 3)) # 0.824
print(round(bilaketa.score(X_test, y_test), 3)) # 0.821

emaitzak = pd.DataFrame(bilaketa.cv_results_)
print(emaitzak[["param_klasifikadorea__C", "mean_test_score",
"std_test_score", "rank_test_score"]].round(3))

print(bilaketa.predict(X_test))

from sklearn.neighbors import KNeighborsClassifier

pipe_knn = Pipeline([
    ("aurre", preprod), 
    ("clf", KNeighborsClassifier())
    ])

param_grid = {"clf__n_neighbors": [1, 3, 5, 7, 11, 15, 21, 31],
              "clf__weights": ["uniform", "distance"]}

g_knn = GridSearchCV(pipe_knn, param_grid, cv=5, scoring="f1")

g_knn.fit(X_train, y_train)

print(g_knn.best_params_) # {'clf__n_neighbors': 31, 'clf__weights': 'uniform'}


lehen_pipeline = Pipeline([
    ("aurreprozesamendua", preprod),
    ("clf", LogisticRegression())
])

param_grid = [
    {
        "clf": [LogisticRegression()], 
        "clf__C" : [0.01, 0.1, 1, 10, 100]
     },
    {
        "clf": [KNeighborsClassifier()], 
        "clf__n_neighbors": [1, 3, 5, 7, 11, 15, 21, 31],
        "clf__weights": ["uniform", "distance"]
    },
    {
        "clf": [DecisionTreeClassifier()],
        "clf__max_depth": [2,3,5]
    }
]

grid_denak = GridSearchCV(lehen_pipeline, param_grid, cv=5,scoring="f1")
grid_denak.fit(X_train, y_train)
print("Denak:")
print(grid_denak.best_params_)


############################1. ARIKETA######################3333
param_grid = [
    {
        "clf": [DecisionTreeClassifier()],
        "clf__max_depth": [2,3,4,5,8],
        "clf__min_samples_leaf": [1,5,10,20]
    }
]

ariketa1 = GridSearchCV(lehen_pipeline, param_grid, cv=5,scoring="recall")
ariketa1.fit(X_train, y_train)
print("Ariketa1:")
print(ariketa1.best_params_)
a1emaitzak = pd.DataFrame(ariketa1.cv_results_)

print(a1emaitzak[["param_clf__max_depth", 
                  "param_clf__min_samples_leaf", 
                  "mean_test_score",
                  "std_test_score", 
                  "rank_test_score"]].round(3))

####################3. ARIKETA#############


from scipy.stats import loguniform
from sklearn.model_selection import RandomizedSearchCV

banaketa = {"clf__C": loguniform(1e-3, 1e3)} ###(0.001, 1000)

a3ausazkoa = RandomizedSearchCV(lehen_pipeline, 
                              banaketa, 
                              n_iter=30, 
                              cv=5, 
                              scoring="recall", 
                              random_state=42)


a3ausazkoa.fit(X_train,y_train)
print(a3ausazkoa.best_params_)

a3emaitzak = pd.DataFrame(a3ausazkoa.cv_results_)

print(a3emaitzak[["param_clf__C","mean_test_score","rank_test_score"]])

