from peewee import Model, CharField, DateTimeField, DecimalField
from database.database import db
import datetime


class Product(Model):
    product = CharField()
    code = CharField(unique=True)
    price = DecimalField()
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
