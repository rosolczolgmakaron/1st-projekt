#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib_iter(n):
    """
    Funkcja wyświetla kolejne wyrazy ciągu fibonacciego.
    Funkcja zwraca n-ty wyraz ciągu.
    F(0) = 0
    F(1) = 1
    F(n) = F(n-2) + F(n-1) dla n>1
    """
    a, b = (0, 1)
    if n == 0:
        print(a)
        return a
    # elif n == 1:
        # print(b)
        # return b
    print(a)
    print(b)
    for i in range(2, n):
        # tmp = b
        # b += a
        # a = tmp
        a, b = b, a + b
        print(a, " Wyraz", i + 1, ": ", b, "ILoraz: ", b / a)

    return b


def fib_iter_2(n):
    a, b = (0, 1)
    i = 2
    while n > 0:
        n -= 1
        i += 1
        a, b = b, a + b
        print(a, b, "Wyraz", i, ":", b, "  ILoraz: ", b / a)


def main(args):

    n = int(input("Podaj zakres: "))
    print(fib_iter_2(n))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
