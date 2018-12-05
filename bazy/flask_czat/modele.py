#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *

baza = SQLiteDatabase('quiz.db')


class BaseModel(MOdel):
    class Meta:
        database = baza


class Pytanie(BaseModel):
    pytanie = Charfield()
    odpowiedz = Charfield()


class Odpowiedz(BaseModel):
    pnr = ForeignKeyField(Pytnaie, related_name='odpowiedzi')
    odpowiedz = CharField()


def main(args):
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
