#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sort_wstaw(lista):
    """wersja liniowa"""
    for i in range(1, len(lista)):
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] < el:  # wyszukanie pozycji
            lista[k + 1] = lista[k]  # przesuwanie elementów w góre tabeli
            k -= 1
        lista[k + 1] = el  # wstawianie elementów
    return lista


def wyszukaj_bin(lewy, prawy, lista, el):

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


def sort_wstaw_bin(lista):
    for i in range(1, len(lista)):
        el = lista[i]
        k = wyszukaj_bin(lewy, prawy, lista, el)
        lista =


def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9]
    print(lista)
    print(sort_wstaw(lista))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
