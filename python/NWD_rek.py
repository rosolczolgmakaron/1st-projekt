#!/usr/bin/env python
# -*- coding: utf-8 -*-


def nwd_rek(a, b):
    if b == 0:
        return a
    return nwd_rek(b, a % b)


def main(args):

    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))

    print("Nwd({:d}, {:d}) = {:d}".format(a, b, nwd_rek(a, b)))

    assert nwd2(19, 114) == 19

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
