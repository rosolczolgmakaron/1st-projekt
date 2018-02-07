#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):
    tekst += (klucz - (len(tekst) % klucz)) * "."
    reszta = len(tekst) % klucz
    # if reszta:
    #     tekst += (klucz - reszta) * "."
    #     print(tekst)
    print(tekst)
    for i in range(klucz):
        # print(tekst(i + ((i-1) * klucz)))
        for j in range(int(len(tekst) / klucz)):
            print(tekst[i + j * klucz])
    return ""

def main(args):
    tekst = input("Podaj tekst: ")
    klucz = int(input("Podaj klucz: "))

    szyfrogram = szyfruj(tekst, klucz)
    print(szyfrogram)
    # print(deszyfruj(szyfrogram, klucz))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
