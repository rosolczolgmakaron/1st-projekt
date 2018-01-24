#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    n = 0
    while n < 2:
        n = int(input("Podaj liczbe: "))

    i = 2
    while i * i <= n:
        if n % i == 0:
            print(n, " jest liczbą złożoną")
            return 0
        i += 1
    print(n, " jest liczbą pierwszą")
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
