#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from uczniowie_model import *


def main(args):
    baza.connect()  # połączenie się z bazą

    kwerendy = [
        'Uczen.select()',
        'Uczen.select().where(Uczen.imie=="Rafał")',
        'Uczen.select().where(Uczen.imie.startswith("G"))',
        'Uczen.select().where(Uczen.egz_mat.between(20,40))',
        'Uczen.select().order_by(uczen.egz_mat.desc())',
    ]

    for obj in eval(kwerendy[3]):
        print(obj.nazwisko, obj.imie, obj.egz_mat)

    baza.commit()
    baza.close()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
