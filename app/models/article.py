# coding: utf-8
from datetime import datetime

from peewee import CharField, DateTimeField, TextField, ForeignKeyField, PrimaryKeyField

from app.models.base import BaseModel


class Article(BaseModel):
    """ Статья в базе знаний """
    class Meta:
        db_table = 'articles'
        evolve = True

    id = PrimaryKeyField(unique=True, index=True)
    title = CharField()
    body = TextField()
    parent = ForeignKeyField('self', related_name='childs', null=True)
    dt = DateTimeField(default=datetime.now())

