#!/usr/bin/env python
# -*- coding: utf-8 -*-


def mnoz(a, b):
    print(a * b)


# (najkrótszy sposób napisania silni)
def mnoz2(*args):  # zmienna lista argumentów
    wynik = 1
    for liczba in args:
        wynik *= liczba
    print(wynik)


def wylicz(imie1='adam', imie2='ewa', **kwargs):
    # ** oznaczają słownik zmiennej długośći;
    # kwargs - key word arguments (nazwa zwyczajowa dla tego typu słownika)
    print(imie1)
    print(imie2)
    for k, v in kwargs.items():
        print('{} {}'.format(k, v))

# TYPY ARGUMENTÓW W FUNKCJI:
# pozycyjne wymagane
# nazwane wymagane
# argumenty domyślne (nie muszą byc wymagane)
# argumenty zmiennej długości


# Kurs C++ odc.16:Struktury danych: stos, kolejka, lista, drzewo binarne
# Pasja Informatyki


def main(args):
    mnoz(4, 6)
    mnoz2(4, 6, 8, 3)
    mnoz2(1, 2, 3, 4, 5, 6, 7)  # 7!
    wylicz(imie2='ola', imie3='piotr', imie4='alfons')
    return 0


if __name__ == '__main__':
    # skrypt został uruchomiony a nie zaimportowany
    import sys
    sys.exit(main(sys.argv))
