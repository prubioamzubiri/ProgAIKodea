import pandas as pd
import numpy as np

df = pd.read_csv("ikasleak_sailkapena.csv")

from sklearn.model_selection import train_test_split

X = df[["ordu_ikasketa", "asistentzia", "aurreko_nota"]]
y = df["arriskuan"]
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.25, random_state=42, stratify=y)

print(y.value_counts().to_dict()) # {0: 239, 1: 161
print(y_test.value_counts().to_dict()) # {0: 60, 1: 40}

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

scaler = StandardScaler()
X_train_esk = scaler.fit_transform(X_train)
X_test_esk = scaler.transform(X_test)

log = LogisticRegression()
log.fit(X_train_esk, y_train)
print(log.score(X_test_esk, y_test)) # 0.85

print(log.predict(X_test_esk[:3])) # [0 0 0]
print(log.predict_proba(X_test_esk[:3]).round(3))
# [[0.514 0.486]
# [0.959 0.041]
# [0.983 0.017]]
# Ikasle berri baten arriskua
berria = pd.DataFrame({"ordu_ikasketa": [6.0], "asistentzia": [85.0],
"aurreko_nota": [5.0]})
print(log.predict_proba(scaler.transform(berria))) # [[0.920 0.080]]


y_arrisku_prob = log.predict_proba(X_test_esk)[:,1]

y_arriskuan = (y_arrisku_prob > 0.3).astype(int)
print(y_arriskuan)

from sklearn.metrics import roc_auc_score, RocCurveDisplay
import matplotlib.pyplot as plt

print(roc_auc_score(y_test, y_arrisku_prob)) 

RocCurveDisplay.from_estimator(log, X_test_esk, y_test)
plt.show()