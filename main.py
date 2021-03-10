from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from models import Biokpi

app = FastAPI()

Biokpi_Pydantic=pydantic_model_creator(Biokpi, name='Biokpi')
BiokpiIn_Pydantic=pydantic_model_creator(Biokpi, name='BiokpiIn', exclude_readonly=True)


@app.get('/')
def index():
    return {'id':'value'}

@app.get('/v1/biokpis')
async def get_biokpis():
    return await Biokpi_Pydantic.from_queryset(Biokpi.all())

@app.get('/v1/biokpis/{biokpi_id}')
async def get_biokpi(biokpi_id: int):
    return await Biokpi_Pydantic.from_queryset_single(Biokpi.get(id=biokpi_id))

@app.post('/v1/biokpis')
async def create_biokpi(biokpi: BiokpiIn_Pydantic):
    biokpi_obj= await Biokpi.create(**biokpi.dict(exclude_unset=True))
    return await Biokpi_Pydantic.from_tortoise_orm(biokpi_obj)


@app.delete('/v1/biokpis/{biokpi_id}')
async def delete_biokpi(biokpi_id: int):
    await Biokpi.filter(id=biokpi_id).delete()
    return {}


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3', # La base de datos que usas
    modules={'models': ['models']}, # Donde estan los modelos
    generate_schemas=True,
    add_exception_handlers=True
)