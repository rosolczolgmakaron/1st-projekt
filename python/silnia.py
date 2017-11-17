#!/usr/bin/env python
# -*- coding: utf-8 -*-
# n! = 1 dla {0,1}
# n! = 1 * 2* ... * n dla n należących do N+ - {0,1}

def silnia_it(n):
    """Funkcja oblicza iteracyjnie silnię l. naturalnej"""
    wynik = 1
    for i in range(2, n+1):
        wynik *= i
    return wynik


def main(args):

    a = int(input("Podaj liczbę: "))

    assert type(a) == int

    assert silnia_it(0) == 1
    assert silnia_it(1) == 1
    assert silnia_it(3) == 6

    print("Silnia = ", silnia_it(a))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
