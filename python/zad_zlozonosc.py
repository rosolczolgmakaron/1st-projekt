#!/usr/bin/env python
# -*- coding: utf-8 -*-


def wypisz_nieparzyste(n):
    for i in range(1, n, 2):
        print(i)


def main(args):
    n = int(input("Podaj wartosc liczby n:"))

    wypisz_nieparzyste(n) 

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
