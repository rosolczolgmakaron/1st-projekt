#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pylab


def main(args):
    ax = pylab.frange(-2, 2, 0.15)  # dziedzina
    ay = []

    for x in ax:
        if x >= 1:
            ay.append(x / (x + 2))
        elif x >= 0:
            ay.append(x**2 / 3)
        else:
            ay.append(x / -3)
    # dla x >= 1 y = x / (x + 2)
    # dla x >= 0 y = x**2 / 3
    # dla x < 0 y = x / -3
    for i in range(len(ax)):
        print('x = {:.2f}, y = {:.2f}'.format(ax[i], ay[i]))

    pylab.plot(ax, ay)
    pylab.title('Wykres funkcji')
    pylab.grid(True)
    pylab.show()
    # rysowanie wykresu funkcji

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
