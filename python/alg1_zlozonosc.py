#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = 0
    while(a < 1 or a > 99):  # wyznaczam poprawny zakres a
        a = int(input("Podaj liczbę: "))

    # for i in range(2, 101, 2):
    #     if a == i:
    #         print("Parzysta")
    #         return 0
    # print("Nieparzysta")

    i = 2
    while (i < 100):
        if a == i:
            print("Parzysta")
            return 0
        i += 2
    print("Nieparzysta")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
