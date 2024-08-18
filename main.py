import pickle
import numpy as np
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel,conlist


app = FastAPI(title="Predicting Wine Class")

# Represents a particular wine (or datapoint)
class Wine(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float


# Represents a batch of wines
class WineBatch(BaseModel):
    batches: List[conlist(item_type=float, min_length=13, max_length=13)]


@app.on_event("startup")
def load_clf():
    # Load classifier from pickle file
    with open("./models/wine.pkl", "rb") as file:
        global clf
        clf = pickle.load(file)


@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over /docs for the API docs"


@app.post("/predict")
def predict(wine: Wine):
    data_point = np.array(
        [
            [
                wine.alcohol,
                wine.malic_acid,
                wine.ash,
                wine.alcalinity_of_ash,
                wine.magnesium,
                wine.total_phenols,
                wine.flavanoids,
                wine.nonflavanoid_phenols,
                wine.proanthocyanins,
                wine.color_intensity,
                wine.hue,
                wine.od280_od315_of_diluted_wines,
                wine.proline,
            ]
        ]
    )

    pred = clf.predict(data_point).tolist()
    pred = pred[0]
    print(pred)
    return {"Prediction": pred}


@app.post("/batch/predict")
def predict(wine: WineBatch):
    batches = wine.batches
    np_batches = np.array(batches)
    pred = clf.predict(np_batches).tolist()
    return {"Prediction": pred}
