
from tortoise import fields
from tortoise.models import Model

class Biokpi(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(max_length=100, unique=True)
    description=fields.TextField()
    units=fields.CharField(max_length=50)
    equation=fields.TextField()
    source=fields.TextField()
    mean=fields.CharField(max_length=50)
    std=fields.CharField(max_length=50)