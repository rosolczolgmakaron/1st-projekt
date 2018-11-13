#!/usr/bin/env python
# -*- coding: utf-8 -*-

# napisz definicję obiektu samochód z nast≥epującymi atrybutami:
# marka
# model
# rok produkcji
# nadwozie
# metody obiektu:
# wiek() - zwraca wiek auta w latach
from datetime import date

dzis = date.today().year


class Auto():
    def __init__(self, marka, model, rok_produkcji, nadwozie):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.nadwozie = nadwozie

    def wiek(self):
        wiek = dzis - self.rok_produkcji
        return wiek


skoda = Auto('Skoda', 'Fabia', 2010, 'Sedan')
print('Wiek samochodu: {} lat'.format(skoda.wiek()))
