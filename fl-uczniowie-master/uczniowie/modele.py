#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py

from peewee import *

baza_plik = 'quiz.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

### MODELE #


class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    klasa = CharField(null=False)
    rok_nab = IntegerField()
    rok_mat = IntegerField()


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')


def main(args):
    baza.connect()  # połączenie z bazą
    baza.create_tables([Klasa, Uczen])  # tworzymy tabele


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
