#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from peewee import *


baza_plik = 'uczniowie_orm.db'
baza = SqliteDatabase(baza_plik)  # instancja wykorzystywanej bazy

######## MODELE ########


class BazaModel(Model):
    class Meta:
        database = baza


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    egz_hum = FloatField(default=0)
    egz_mat = FloatField(default=0)
    egz_jez = FloatField(default=0)
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')


class Klasa(BazaModel):
    klasa = CharField(null=False)
    rok_naboru = IntegerField(default=0)
    rok_matury = IntegerField(default=0)


class Przedmiot(BazaModel):
    przedmiot = CharField()
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = BooleanField()


class Oceny(BazaModel):
    datad = DateField()
    id_uczen = IntegerField(default=0)
    id_przedmiot = IntegerField(default=0)
    ocena = DecimalField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')


def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  # połączenie się z bazą
    baza.create_tables([Uczen, Klasa, Przedmiot, Oceny])  # tworzymy tabele

    # kl3A = Klasa()  # instancja czyli oniekt klasy
    # kl3A.nazwa = '3A'
    # kl3A.roknaboru = 2010
    # kl3A.rokmatury = 2013
    # kl3A.save()
    # kl2A = Klasa(nazwa='2A', roknaboru=2009, rokmatury=2012)
    # kl2A.save()
    # ucz1 = Uczen(imie='Adam', nazwisko='Słodowy', plec=False, klasa=kl3A)
    # ucz1.save()
    # ucz2 = Uczen(imie='Ewa', nazwisko='Kolorowa', plec=True, klasa=kl2A)
    # ucz2.save()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
