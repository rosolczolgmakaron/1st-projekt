#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def losuj(ileliczb, maksliczb):
    liczby = []
    ile = 0 # ilośc wylososwanych liczb
    while ile < ileliczb:
    # for i in range(ileliczb):
        liczba = randint(0, maksliczb)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            ile += 1
    print(liczby)


def main(args):
    ileliczb = int(input("Ile liczb chcesz zgadnąć? "))
    maksliczb = int(input("Podaj górny zakres: "))

    losuj(ileliczb, maksliczb)

    typy = set()  # pusty zbiór
    for i in range(ileliczb):
        typ = input("Podaj typ: ")
        typy.add(typ)

    print(typy)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
