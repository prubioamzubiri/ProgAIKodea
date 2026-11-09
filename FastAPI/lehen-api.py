from fastapi import FastAPI

app = FastAPI(title="Zereginen APIa")

@app.get("/agurra")
def hasiera():
    return {"mezua": "Kaixo , Pablo naiz!"}

@app.get("/kurtsoa")
def hasiera():
    return {"mezua": "AABD kurstoa egiten ari naiz"}

@app.get("/agurra/{izena}")
def agurra(izena):
    return {"mezua": f"Kaixo , {izena}!"}

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier



#/score -> KNN batazbesteko scorea cv=5ekin

iris = load_iris()

X = iris.data
y = iris.target

emaitza = cross_val_score(KNeighborsClassifier(n_neighbors=7), 
                         X, 
                         y,
                         cv=5,  
                         scoring="accuracy")


@app.get("/score")
def score():
    return {"score": emaitza.mean()}


modelo = KNeighborsClassifier(n_neighbors=7)
modelo.fit(X,y)

@app.get("/predict")
def predict (largo_sepalo : float, 
             ancho_sepalo: float, 
             largo_petalo: float, 
             ancho_petalo:float):

    prediccion = modelo.predict([[largo_sepalo,
                                 ancho_sepalo,
                                 largo_petalo,
                                 ancho_petalo]])
    
    return {"erantzuna": f"{iris.target_names[prediccion]}"}

from zeregina import ZereginBerria, Zeregina

zereginak: dict[int, Zeregina] = {} # memorian
hurrengo_id = 1

from fastapi import Query, HTTPException

@app.get("/zereginak", response_model=list[Zeregina])
def zerrenda(egina: bool | None = None,
             muga: int = Query(10, ge=1, le=100)):
    
    emaitza = list(zereginak.values())
    if egina is not None:
        emaitza = [z for z in emaitza if z.egina == egina]
    return emaitza[:muga]

@app.get("/zereginak/kopurua")
def kopurua():
    return {"kopurua" : f"{len(zereginak)}"}

@app.get("/zereginak/{zeregin_id}", response_model=Zeregina)
def bat_lortu(zeregin_id: int):
    if zeregin_id not in zereginak:
        raise HTTPException(status_code=404, detail="Zeregina ez da aurkitu")
    return zereginak[zeregin_id]

@app.post("/zereginak", response_model=Zeregina , status_code=201)
def sortu(berria: ZereginBerria):

    global hurrengo_id    
    zeregina = Zeregina(id=hurrengo_id, 
                        izenburua = berria.izenburua,
                        egina = berria.egina)
    
    zereginak[zeregina.id] = zeregina
    hurrengo_id += 1
    return zeregina

@app.put("/zereginak/{zeregin_id}", response_model=Zeregina)
def ordezkatu(zeregin_id: int, datuak: ZereginBerria):
    if zeregin_id not in zereginak:
        raise HTTPException(status_code=404, detail="Ez da aurkitu")
    zereginak[zeregin_id] = Zeregina(id=hurrengo_id, 
                                     izenburua = datuak.izenburua,
                                     egina = datuak.egina)
    return zereginak[zeregin_id]

@app.delete("/zereginak/{zeregin_id}", status_code=204)
def ezabatu(zeregin_id: int):
    if zeregin_id not in zereginak:
        raise HTTPException(status_code=404, detail="Ez da aurkitu")
    del zereginak[zeregin_id]

