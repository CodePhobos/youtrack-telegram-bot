from peewee import Model
from classes import PostgresDB

class AbstractModel(Model):
    class Meta:
        database = PostgresDB
