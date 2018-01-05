#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import floor


def wyszukaj_liniowo(lista, el):
    for i in range(0, len(lista)):
        if lista[i] == el:
            return i
    return -1


def wyszukaj_binarnie(lista, el):

    lewy, prawy = 0, len(lista) - 1
    while lewy < prawy:
        sr = floor((lewy + prawy) / 2)
        if el <= lista[sr]:
            prawy = sr
        else:
            lewy = sr + 1
    if lista[lewy] == el:
        return lewy

    return -1


def wyszukaj_bin_rek(lewy, prawy, lista, el):
    if lewy > prawy:
        return -1
    sr = floor((lewy + prawy) / 2)
    if el == lista[sr]:
        return sr
    if el < lista[sr]:
        return wyszukaj_bin_rek(lewy, sr - 1, lista, el)
    else:
        return wyszukaj_bin_rek(sr + 1, prawy, lista, el)


def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9]
    lista.sort()
    print(lista)
    el = 0

    # print(wyszukaj_liniowo(lista, el))
    # assert wyszukaj_liniowo(lista, 8) == -1

    print(wyszukaj_binarnie(lista, el))
    print(wyszukaj_bin_rek(0, len(lista) - 1, lista, el))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
