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


def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9]
    print(lista)
    # [3, 4, 7, 0, 2, 3, 1, 9]
    # [3, 4, 7, 0, 2, 3, 1, 9]
    # [0, 3, 4, 7, 2, 3, 1, 9]
    # [0, 2, 3, 4, 7, 3, 1, 9]
    # [0, 2, 3, 3, 4, 7, 1, 9]
    # [0, 1, 2, 3, 3, 4, 7, 9]
    # [0, 1, 2, 3, 3, 4, 7, 9]
    print(sort_wstaw(lista))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
