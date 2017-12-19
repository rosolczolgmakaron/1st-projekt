#!/usr/bin/env python
# -*- coding: utf-8 -*-


def wynik(n, tb):
    # n-wyraz ciągu
    # tb- tablica
    while n > 0:
        if n == 1:
            return tb[0]
        return wynik(n - 1, tb) * tb[n - 1]


def main(args):
    tb = []
    n = int(input("Podaj wartośc n: "))

    print("Wynik: ", wynik(n, tb))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
