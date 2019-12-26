# coding: utf-8

from peewee import Model

from app import db


class BaseModel(Model):
    """ Базовый класс для моделей приложения """

    class Meta:
        database = db
        evolve = False