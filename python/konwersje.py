#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dec2other(liczba10, podstawa):
    """Konwersja liczby dziesiętnej na system o podanej podstawie """
    liczba = []
    while liczba10 != 0:
        reszta = liczba10 % podstawa
        if reszta > 9:  # wykorzystanie kodu ASCII
            reszta = chr(reszta + 55)
        liczba.append(str(reszta))  # dodanie do listy
        liczba10 = int(liczba10 / podstawa)
    liczba.reverse()  # odwrócenie listy
    return "".join(liczba)  # połączenie wyrazów listy


def zamiana1():
    """Pobranie danych wejściowych"""
    liczba = int(input("Podaj liczbe: "))
    podstawa = int(input("Podaj podstawe: "))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawe: "))
    print("Wynik konwersji: {}(10) = {}({})".format(
        liczba, dec2other(liczba, podstawa), podstawa))


def other2dec(liczba, podstawa):
    """Zamiana podanej liczby na system dziesiety"""
    liczba10 = 0
    potega = len(liczba) - 1
    for cyfra in liczba:
        if not cyfra.isdigit():
            liczba10 += (ord(cyfra.upper()) - 55) * (podstawa ** potega)
            # liczba10 += (ord(cyfra) - 55) * (podstawa ** potega)
            # ** - potega
        else:
            # ** to operator potegowania
            liczba10 += int(cyfra) * (podstawa ** potega)
        potega -= 1
    return liczba10


def zamiana2():
    """Pobranie danych wejściowych"""
    liczba = input("Podaj liczbe: ")
    podstawa = int(input("Podaj podstawe: "))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawe: "))
    if podstawa > 9:
        for i in liczba:
            if ord(i.upper()) > 70:
                print("Zły format danych wejsciowych")
                return 0
    else:
        for i in liczba:
            if int(i) >= podstawa:
                print("Liczba nie moze skladac sie z cyfr > podstawy")
                return 0
    print("Wynik konwersji: {}({}) = {}(10)".format(
        liczba, podstawa, other2dec(liczba, podstawa)))


def main(args):
    print("Zamiana liczby dziesiętnej na liczbę o podanej podstawie"
          "<2;16> lub odwrotnie")
    zamiana1()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
