#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import randint


def minmax(lista):
    lmin = []
    lmax = []
    i = 0
    for i in range(int(len(lista)/2)):
        if lista[i] > lista[i+1]:
            lmin.append(lista[i+1])
            lmin.append(lista[i])
        else:
            lmin.append(lista[i])
            lmax.append(lista[i+1])



def minimum(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min


def maximum(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max


def losuj(ile, zakres):
    lista = []
    for i in range(ile):
        lista.append(randint(0, zakres))
    return lista


def main(args):
    ile = 20
    zakres = 50
    lista = losuj(ile, zakres)
    print(lista)
    print("minimum:", minimum(lista))
    print("Maximum:", maximum(lista))
    print(lista[indeks], lista[indeks + 1])
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
