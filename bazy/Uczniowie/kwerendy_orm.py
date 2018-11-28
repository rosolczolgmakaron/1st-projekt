#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py
import os
from uczniowie_model import *


def kw08():
    """Lista nazwisk uczniów i nazw klas"""
    query = (Uczen
             .select(Uczen.nazwisko, Uczen.klasa.klasa)
             .join(Klasa)
             )
    for obj in query:
        print(obj.nazwisko, obj.klasa.klasa)


def kw09():
    """Lista klas i ilość uczniów"""
    query = (Uczen
             .select(fn.Count(Uczen.id).alias('ilu'), Uczen.klasa.klasa)
             .join(Klasa)
             .group_by(Klasa)
             .order_by(SQL('ilu').desc()))
    for obj in query:
        print(obj.klasa.klasa, obj.ilu)


def kw10():
    """Lista przedmiotów i ilość ocen"""
    query = (Ocena
             .select(fn.Count(Ocena.ocena).alias('ile'), Ocena.przedmiot.przedmiot)
             .join(Przedmiot)
             .group_by(Przedmiot)
             .order_by(SQL('ile').desc()))
    for obj in query:
        print(obj.przedmiot.przedmiot, obj.ile)


def kw11():
    """Suma wszystkich ocen"""
    pass


def main(args):
    baza.connect()  # połączenie z baża

    kwerendy = [
        "Uczen.select()",
        "Uczen.select().where(Uczen.imie=='Rafał')",
        "Uczen.select().where(Uczen.imie.startswith('G'))",
        "Uczen.select().where(Uczen.egz_mat.between(20, 40))",
        "Uczen.select().where((Uczen.nazwisko=='Piasecki') & (Uczen.imie=='Rafał'))",
        "Uczen.select().order_by(Uczen.egz_mat.asc())",
        "Uczen.select().where(Uczen.plec==1).order_by(Uczen.egz_mat.asc())",
    ]

    # for obj in eval(kwerendy[6]):
    #     print(obj.nazwisko, obj.imie, obj.egz_mat)
    kw10()

    baza.commit()
    baza.close()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
