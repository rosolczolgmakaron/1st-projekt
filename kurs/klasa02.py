#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Osoba():
    """Prosta klasa opisująca osobę"""

    def __init__(self, imie, nazwisko, hp):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ustawPlec(imie)
        self.hp = hp

    def ustawPlec(self, imie):
        if imie[-1] == 'a':
            # __ - ukrycie atrybutu; atrybut prywatny;
            # niemożliwy do odczytu
            self.__plec = 'k'
            self.__atak = 3
            self.__blok = 1
        else:
            self.__plec = 'm'
            self.__atak = 5
            self.__blok = 2

    def atakuj(self, osoba):
        # osoba.hp -= self.atak
        osoba.blokuj(self.__atak)

    def blokuj(self, atak):
        self.hp -= (atak - self.__blok)
        if self.hp < 1:
            print('YOU DIED!')
        else:
            print('I am still alive! Hit me baby one more time!')


jakub = Osoba('Jakub', 'Gwizd', 10)  # nazwa obiektu i jego atrybuty;
jakub.wzrost = 170
print(jakub.__dict__)  # pokazuje wszystkie atrybuty klasy jako słownik

michal = Osoba('Michał', 'Świst', 10)
print(michal.__dict__)

print('Combat: ')
jakub.atakuj(michal)
michal.atakuj(jakub)
print('Hp Jakub: {} , Hp Michał: {}'.format(jakub.hp, michal.hp))
