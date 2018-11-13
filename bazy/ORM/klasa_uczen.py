#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from peewee import *


baza_plik = 'test_orm.db'
baza = SqliteDatabase(baza_plik)  # instancja wykorzystywanej bazy

######## MODELE ##########


class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    liczba_uczniow = IntegerField(default=0)


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')


class Wynik(BazaModel):
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')


def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  # połączenie się z bazą
    baza.create_tables([Klasa, Uczen, Wynik])  # tworzymy tabele

    kl3A = Klasa()  # instancja czyli oniekt klasy
    kl3A.nazwa = '3A'
    kl3A.roknaboru = 2010
    kl3A.rokmatury = 2013
    kl3A.save()
    kl2A = Klasa(nazwa='2A', roknaboru=2009, rokmatury=2012)
    kl2A.save()
    ucz1 = Uczen(imie='Adam', nazwisko='Słodowy', plec=False, klasa=kl3A)
    ucz1.save()
    ucz2 = Uczen(imie='Ewa', nazwisko='Kolorowa', plec=True, klasa=kl2A)
    ucz2.save()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
