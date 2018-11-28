#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stos:
    def __init__(self, maks=20):  # kostruktor
        self.elementy = []
        self.maks = maks
        self.ostatni = 0

    def isEmpty(self):
        return self.elementy == []

    def push(self, element):
        if self.ostatni >= self.maks:
            print('Stack overflow!')
            return False
        self.elementy.append(element)
        self.ostatni += 1
        return True

    def pop(self):
        if self.ostatni < 1:
            print('Stack empty!')
            return False
        self.ostatni -= 1
        return self.elementy.pop()

    def peek(self):
        if self.ostatni < 1:
            print('Stack empty!')
            return ''
        return self.elementy[self.ostatni - 1]


def main(args):
    s = Stos()
    s.push(1)
    s.push(6)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
