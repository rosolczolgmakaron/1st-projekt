#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    i = 0
    a = int(input("Wpisz ile razy chcesz wykonać pomiar bmi: "))

    while (i < a):
        i += 1
        masa = float(input("Podaj swoją masę: "))
        wzrost = float(input("Podaj swój wzrost w centymetrach: "))
        bmi = masa / (wzrost * wzrost) * 10000
        if bmi < 18.5:
            print("niedowaga")
        elif bmi < 24.9:
            print("norma")
        elif bmi < 30:
            print("nadwaga")
        elif 30 <= bmi:
            print("otyłość")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
