#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a0 = 1
# a1 = a
# an = a * ... * a (n-czynników) dla n należących do N+ - {0,1}

def potega_it(podst, wykladnik):
    """Funkcja oblicza iteracyjnie potęgę l. naturalnej"""
    wynik = 1
    for i in range(wykladnik):
        wynik *= podst
    return wynik


def main(args):
    # pobierz od użytkownika podstawe i wykładnik i przypisz do odpowiednich zmiennych
    # wywołaj funkcje potega_it()
    podst = int(input("Podaj podstawę: "))
    wykladnik = int(input("Podaj wykładnik: "))
    assert type(podst) == int
    assert type(wykladnik) == int

    assert potega_it(100, 0) == 1
    assert potega_it(100, 1) == 100
    assert potega_it(2, 3) == 8

    print("Potęga = ", potega_it(podst, wykladnik))
    #wynik = potega_it(podst, wykladnik)
    #print("Potęga = ", wynik)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
