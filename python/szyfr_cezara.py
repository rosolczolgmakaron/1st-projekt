#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):
    """
    Szyfrowanie tekstu za pomocą szyfru Cezara
    """
    szyfrogram = ""
    klucz %= 26
    for znak in tekst:
        ascii = ord(znak) + klucz
        if ascii > 90:
            ascii -= 26
        szyfrogram += chr(ascii)
    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    tekst = ""
    pass
    return tekst
# dokończyć funkcje deszyfruj
# obsłużyć małe i duże litery
# obsługa zdań o dużych i małych literach, spacje powinny być niekodowane
# na 6 - obsłużyć polskie znaki

def main(args):
    tekst = input("Podaj tekst: ")
    klucz = int(input("Podaj klucz: "))
    szyfrogram = szyfruj(tekst, klucz)
    print(szyfrogram)
    print(deszyfruj(szyfrogram, klucz))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
