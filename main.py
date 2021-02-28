from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class Biokpi(BaseModel):
    name: str
    key: str
    description: str
    bibliography: str
    normalValues: str
    criticalValues: str

@app.get('/')
def index():
    return {'key':'value'}

@app.get('/biokpis')
def get_biokpis():
    return db

@app.get('/biokpis/{biokpi_id}')
def get_biokpi(biokpi_id: int):
    return db[biokpi_id-1]

@app.post('/biokpis')
def create_biokpi(biokpi: Biokpi):
    db.append(biokpi.dict())
    return db[-1]

@app.delete('/biokpis/{biokpi_id}')
def delete_biokpi(biokpi_id: int):
    db.pop(biokpi_id-1)
    return {}