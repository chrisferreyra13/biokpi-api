from fastapi import FastAPI
from pydantic import BaseModel

from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

app = FastAPI()

db = []

class Biokpi(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(100, unique=True)
    description=fields.TextField()
    bibliography=fields.TextField()
    normalValues=fields.CharField(50, unique=True)
    criticalValues=fields.CharField(50, unique=True)

Biokpi_Pydantic=pydantic_model_creator(Biokpi, name='Biokpi')
BiokpiIn_Pydantic=pydantic_model_creator(Biokpi, name='BiokpiIn', exclude_readonly=True)

'''class Biokpi(BaseModel):
    name: str
    key: str
    description: str
    bibliography: str
    normalValues: str
    criticalValues: str'''

@app.get('/')
def index():
    return {'key':'value'}

@app.get('/biokpis')
def get_biokpis():
    return db

@app.get('/biokpis/{biokpi_id}')
def get_biokpi(biokpi_id: int):
    return db[biokpi_id-1]

'''@app.post('/biokpis')
def create_biokpi(biokpi: Biokpi):
    db.append(biokpi.dict())
    return db[-1]
'''

@app.delete('/biokpis/{biokpi_id}')
def delete_biokpi(biokpi_id: int):
    db.pop(biokpi_id-1)
    return {}


register_tortoise(
    app,
    db='sqlite://db.sqlite3',
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)