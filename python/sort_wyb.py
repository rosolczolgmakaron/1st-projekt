#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


def losuj(liczby, n, m):
    # n - ilość liczb
    # m - maksymalna ilośc liczb
    ile = 0

    while ile < n:
        a = random.randint(0, m)
        if liczby.count(a) == 0:
            liczby.append(a)
            ile += 1

    return liczby


def sort_wyb(tab):
    for i in range(len(tab)):
        k = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[k]:
                k = j
        tab[i], tab[k] = tab[k], tab[i]
    return tab


def main(args):
    ile = 10
    tab = []
    m = int(input('Podaj maksymalną liczbe: '))
    print(losuj(tab, ile, m))
    print(sort_wyb(tab))
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
