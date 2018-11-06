#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def main(args):
    a, b, c = eval(input('Podaj boki trójkąta oddzielone przecinkami: '))
    print('Podano boki: {}, {}, {}'.format(a, b, c))
    trojkat = False
    if a + b > c:
        if a + c > b:
            if b + c > a:
                trojkat = True
    if trojkat:
        print('Da się zbudować trójkąt!')
        p = (a + b + c) / 2
        pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('Pole trójkąta o bokach {}, {}, {}'.format(
            a, b, c), ': ', '{:.4f}'.format(pole))
        if (a**2 + b**2 == c**2) or \
            (a**2 + c**2 == b**2) or \
                (c**2 + b**2 == a**2):
            print('Trójkąt jest prostokątny!')
        else:
            print('Trójkąt nie jest prostokątny!')
    else:
        print('Nie da sie!')

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
