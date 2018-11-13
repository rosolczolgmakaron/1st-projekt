#!/usr/bin/env python
# -*- coding: utf-8 -*-

stos = []  # pusta lista, zasięg globalny
SP = 0  # stack pointer - wskaźnik wierzchołka


def push(rozmiar, dane):
    global stos, SP
    if SP < rozmiar:
        stos[SP] = dane
        SP += 1  # inkrementacja
    else:
        print('Stack overflow!')  # przepełnienie stosu


def pop(rozmiar):
    global stos, SP
    SP -= 1  # dekrementacja
    if SP >= 0:
        print(stos[SP])
        stos[SP] = None
    else:
        print('Stack overflow!')


def main(args):
    global stos, SP
    rozmiar = int(input('Podaj rozmiar stosu: '))
    stos = [None] * rozmiar  # inicjacja stosu
    # wkładanie danych na stos
    push(rozmiar, 1)
    push(rozmiar, 2)
    push(rozmiar, 3)
    push(rozmiar, 4)
    push(rozmiar, 5)
    push(rozmiar, 6)
    pop(rozmiar)
    pop(rozmiar)
    pop(rozmiar)
    pop(rozmiar)

    print(stos)
    print('SP = ', SP)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
