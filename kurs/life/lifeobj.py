#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys


class Plansza():
    """ Plansza gry """

    def __init__(self, szer, wys):
        """ Konstruktor, przygotowanie okna gry """
        self.pow = pygame.display.set_mode((szer, wys), 0, 32)
        self.szer = szer
        self.wys = wys
        pygame.display.set_caption('Gra w życie')

    def rysuj(self, *args):
        """ Rysowanie okna gry """
        # kolor okna gry, składowe RGB podane w tupli
        self.pow.fill((0, 0, 0))
        for obj in args:
            obj.rysuj_na(self.pow)
        pygame.display.update()


class LifeGra(object):
    """ Kontroler gry """

    def __init__(self, szer, wys, roz=10):
        pygame.init()
        self.plansza = Plansza(szer * roz, wys * roz)
        self.populacja = Populacja(szer, wys, roz)

    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN:
                self.populacja.obsluz_mysze()
            self.plansza.rysuj(self.populacja)


DEAD = 0
ALIVE = 1


class Populacja():
    def __init__(self, szer, wys, roz=10):
        self.roz, self.szer, self.wys = roz, szer, wys
        self.generacja = self.utworz_generacje()

    def utworz_generacje(self):
        # generacja = []
        # for x in range(self.szer):
        #     kolumna = []
        #     for y in range(self.wys):
        #         kolumna.append(DEAD)
        #     generacja.append(kolumna)
        # return generacja
        return [[DEAD for y in range(self.wys)] for x in range(self.szer)]

    def obsluz_mysze(self):
        przyciski = pygame.mouse.get_pressed()
        if not any(przyciski):
            return
        x, y = pygame.mouse.get_pos()
        x /= self.roz
        y /= self.roz
        stan = True if przyciski[0] else False
        print(stan)
        self.generacja[int(x)][int(y)] = ALIVE if stan else DEAD

    def rysuj_na(self, pow):
        for x, y in self.zywe_komurki():
            roz = (self.roz, self.roz)
            pozycja = (x * self.roz, y * self.roz)
            kolor = (255, 255, 255)
            grubosc = 1
            pygame.draw.rect(pow, kolor, Rect(pozycja, roz), grubosc)

    def zywe_komurki(self):
        """Generator zwracający współrzędne żywych komurek"""
        for x in range(len(self.generacja)):
            kolumna = self.generacja[x]
            for y in range(len(kolumna)):
                if kolumna[y] == ALIVE:
                    yield x, y

    def zwroc_sasiada(self, x, y):
        """Generator zwracający sąsiadów komurki"""
        # lx = list(range(x - 1, x + 2))
        # [[(a,b) for b in lx] for a in  lx]
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue  # pomijamy badaną komurke
                elif i < 0:
                    i = self.szer - 1
                if j >= self.wys:
                    j = 0
                elif j < 0:
                    j = self.wys - 1
                yield self.generacja[i][j]


if __name__ == "__main__":
    gra = LifeGra(80, 40)
    gra.uruchom()
