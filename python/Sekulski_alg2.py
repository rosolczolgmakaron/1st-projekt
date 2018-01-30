#!/usr/bin/env python
# -*- coding: utf-8 -*-


def czy_parzysta(a):
    i = 2
    while(i > a):  # while not(i > a) # uzywając pętli while każdej wartości zwracane jest "liczba nieparzysta"
        if a == i:
            print("liczba parzysta")
            return
        i += 2
    print("liczba nieparzysta")


def main(args):

    a = int(input("Podaj liczbe: "))
    while a < 0 or a > 100:
        print (a)

    czy_parzysta(a)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
