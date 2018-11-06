#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bmi(m, w):
    return m / (w / 100)**2


def main(args):
    masa, wzrost = eval(
        input('Podaj masę w kg i wzrost w cm oddzielająć wartości przecinkami: '))
    a = bmi(masa, wzrost)
    print('Bmi: {:.2f}'.format(a))
    if a < 18.5:
        print('niedowaga')
    elif a < 24.9:
        print('norma')
    elif a < 30:
        print('nadwaga')
    elif 30 <= a:
        print('otyłość')
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
