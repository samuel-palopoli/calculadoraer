from peewee import AutoField, CharField, Model

from config.database import database

class ResidenciaDB(Model):
    id = AutoField()
    proprietario = CharField()

    class Meta:
        database = database

