from fastapi import FastAPI, status, Depends
from pydantic import BaseModel
import uvicorn
import joblib

app = FastAPI(title="API Startup", version="1.0")


## Basemodel
class StartupData(BaseModel):
    rd: float = 165349.2
    administration: float = 136897.8
    marketing: float = 471784.1


## blocco per la cache del mio modello
@app.on_event("startup")
def startup_event():
    "modello *.pkl di ML"
    global model  # la varibile dovrà essere globale
    model = joblib.load("model.pkl")
    print(" MODEL LOADED!!")
    return model


@app.get("/")
def home():
    return {"Welcome!"}


@app.get("/predict")
def predict_get(data: StartupData = Depends()):
    try:
        X = [[data.rd, data.administration, data.marketing]]
        pred = round(model.predict(X)[0], 2)
        return pred
    except:
        raise HTTPException(status_code=404, detail="error")


@app.post("/predict")
def predict_post(data: StartupData):
    try:
        X = [[data.rd, data.administration, data.marketing]]
        pred = round(model.predict(X)[0], 2)
        return pred
    except:
        raise HTTPException(status_code=404, detail="error")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
