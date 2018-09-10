#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dodaj(a, b):
    wynik = a + b
    return wynik


def odejmij(a, b):
    wynik = a - b
    return wynik


def pomnoz(a, b):
    wynik = a * b
    return wynik


def dziel(a, b):
    wynik = 0
    if (b != 0):
        wynik = a / b
    else:
        print("Math ERROR")
    return wynik


def main(args):
    i = 1
    while (i != 0):
        a = int(input("Podaj pierwszą liczbę: "))
        znak = input("Podaj znak: ")
        b = int(input("Podaj drugą liczbę: "))
        wynik = 0
        if znak == '+':
            wynik = dodaj(a, b)
        elif znak == '-':
            wynik = odejmij(a, b)
        elif znak == '*':
            wynik = pomnoz(a, b)
        elif znak == '/':
            wynik = dziel(a, b)
        print(wynik)
        i = input("Czy chcesz kontynuować prace z kalkulatorem? tak(1)/nie(0): ")


    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
