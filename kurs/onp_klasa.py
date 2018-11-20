#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stos_obj import Stos


class ONPKlasa(Stos):

    def __init__(self, onp_str='', a_str=''):
        super().__init__(10)
        if not self.czy_poprawne(onp_str):
            print('Błąd wyrażenia')
            onp_str = ''
        self.onp_str = onp_str
        self.a_str = a_str
        self.log = []
        self.wynik = None

    def czy_poprawne(self, onp):
        for el in onp:
            if el.isalpha():
                return False
        return True

    def oblicz_onp(self):
        onp = self.onp_str.split(' ')

        for el in onp:
            if el.isdigit():
                self.push(el)
            else:
                a = self.pop()
                b = self.pop()
                if el == '/' and a == '0':
                    print('ZeroDivisionError!')
                    return 0
                else:
                    self.log.append(str((b + el + a)))
                    self.push(str(eval(b + el + a)))
        self.wynik = self.pop()

    def p(self, operator):  # priorytet
        if operator == '(':
            return 0
        if operator == '+' or '-':
            return 1
        if operator == '*' or '/':
            return 2
        if operator == '**':
            return 3

    def a2onp(self):
        operatory = set(['+', '-', '*', '/', '**'])
        for znak in self.a_str:
            print('Badamy znak: ', znak)
            if znak == ' ':
                continue
            elif znak == '(':
                self.push(znak)
            elif znak == ')':
                while self.peek() != '(':
                    self.onp_str += self.pop() + ' '
                self.pop()  # usunięcie nawiasu zamykająćego ze stosu
            elif znak in operatory:
                while not self.isEmpty():
                    if self.p(znak) == 3 or self.p(znak) > self.p(self.peek()):
                        break
                    self.onp_str += self.pop()
                self.push(znak)
            else:
                self.onp_str += znak + ' '
        while self.peek():
            self.onp_str += self.pop() + ' '
        self.onp_str.strip()


def main(args):
    # onp = input('Podaj wyr. ONP, oddzielając operandy i operatory spacjami;\n')
    # ol = ONPKlasa(onp)
    # ol.oblicz_onp()
    # print('Obliczenia: ', ol.log)
    # print('Wynik: ', ol.wynik)

    o2 = ONPKlasa(a_str='(4+5)*6')
    o2.a2onp()
    print('ONP:', o2.onp_str)
    o2.oblicz_onp()
    print('Obliczenia: ', o2.log)
    print('Wynik: ', o2.wynik)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
