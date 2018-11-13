#!/usr/bin/env python
# -*- coding: utf-8 -*-

stos = []  # pusta lista, zasięg globalny
SP = 0  # stack pointer - wskaźnik wierzchołka


def push(stos, rozmiar, SP, dane):
    if SP < rozmiar:
        stos[SP] = dane
        SP += 1  # inkrementacja
    else:
        print('Stack overflow!')  # przepełnienie stosu
    return SP


def pop(stos, rozmiar, SP):
    element = None
    SP -= 1  # dekrementacja
    if SP >= 0:
        element = (stos[SP])
        stos[SP] = None
    else:
        print('Stack overflow!')
    return SP, element


def main(args):
    stos = []  # pusta lista, zasięg lokalny
    SP = 0  # stack pointer - wskaźnik wierzchołka
    rozmiar = int(input('Podaj rozmiar stosu: '))
    stos = [None] * rozmiar  # inicjacja stosu
    # wkładanie danych na stos
    SP = push(stos, rozmiar, SP, 1)
    SP = push(stos, rozmiar, SP, 2)
    SP = push(stos, rozmiar, SP, 3)
    SP = push(stos, rozmiar, SP, 4)
    SP, element = pop(stos, rozmiar, SP)
    print(element)
    SP, element = pop(stos, rozmiar, SP)
    print(element)
    SP, element = pop(stos, rozmiar, SP)
    print(element)

    print(stos)
    print('SP = ', SP)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
