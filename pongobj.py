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
        pygame.display.set_caption('Pong')

    def rysuj(self, *args):
        """ Rysowanie okna gry """
        # kolor okna gry, składowe RGB podane w tupli
        self.pow.fill((200, 255, 255))
        for obGraf in args:
            self.pow.blit(obGraf.pow, obGraf.prost)
        pygame.display.update()


class PongGra(object):
    """ Kontroler gry """

    def __init__(self, szer, wys):
        pygame.init()
        pygame.key.set_repeat(50, 25)
        self.plansza = Plansza(szer, wys)
        self.pal1 = Paletka(szer=100, wys=20, x=350, y=360)
        self.pal2 = Paletka(szer=100, wys=20, x=350, y=20, kolor=(255, 0, 0))
        # self.pal3 = Paletka(szer=20, wys=100, x=20, y=150, kolor=(255, 0, 0))
        self.pilka = Pilka(szer=20, wys=20, x=390, y=190, kolor=(0, 0, 255))
        self.gracz2 = Gracz2(self.pal2, self.pilka, 5)
        # zegar
        self.fpsClock = pygame.time.Clock()

    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEMOTION:
                    mX, mY = event.pos
                    self.pal1.przesun(mX, self.plansza.szer)

                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.pal1.przesun2(self.plansza.szer, 10)
                    elif event.key == K_LEFT:
                        self.pal1.przesun2(self.plansza.szer, -10)
                    elif event.key == K_UP:
                        self.pal1.przesun3(self.plansza.wys, -10)
                    elif event.key == K_DOWN:
                        self.pal1.przesun3(self.plansza.wys, 10)

            self.pilka.ruszaj(self.plansza.szer,
                              self.plansza.wys, self.pal1, self.pal2)
            self.gracz2.ruszaj()
            self.plansza.rysuj(
                self.pal1,
                self.pal2,
                # self.pal3
                self.pilka
            )
            self.fpsClock.tick(120)


class ObiektGraf():
    """Klasa bazowa dla rysowanych obiektów"""

    def __init__(self, szer, wys, x, y, kolor=(0, 255, 0)):
        self.szer = szer
        self.wys = wys
        self.pow = pygame.Surface([szer, wys], pygame.SRCALPHA).convert_alpha()
        self.prost = self.pow.get_rect(x=x, y=y)
        self.kolor = kolor


class Paletka(ObiektGraf):
    def __init__(self, szer, wys, x, y, kolor=(0, 255, 0), maks_v=10):
        super().__init__(szer, wys, x, y, kolor)
        self.pow.fill(kolor)
        self.maks_v = maks_v

    def przesun(self, mX, o_szer):
        """
        :param:
        mX = składowa x pozycji paletki
        o_szer = szerokość okna gry
        """
        przesuniecie = mX - self.maks_v
        if przesuniecie > o_szer - self.szer:
            przesuniecie = o_szer - self.szer
        if przesuniecie < 0:
            przesuniecie = 0
        self.prost.x = przesuniecie

    def przesun2(self, o_szer, krok):
        przesuniecie = self.prost.x + krok
        if przesuniecie > o_szer - self.szer:
            przesuniecie = o_szer - self.szer
        if przesuniecie < 0:
            przesuniecie = 0
        self.prost.x = przesuniecie

    def przesun3(self, o_wys, krok):
        przesuniecie = self.prost.y + krok
        if przesuniecie > o_wys - self.wys:
            przesuniecie = o_wys - self.wys
        if przesuniecie < 0:
            przesuniecie = 0
        self.prost.y = przesuniecie

class Pilka(ObiektGraf):
    def __init__(self, szer, wys, x, y, kolor=(0, 0, 255), px_v=3, py_v=3):
        super().__init__(szer, wys, x, y, kolor)
        pygame.draw.ellipse(self.pow, self.kolor, [0, 0, self.szer, self.wys])
        self.px_v = px_v
        self.py_v = py_v
        self.start_x = x
        self.start_y = y

    def ruszaj(self, o_szer, o_wys, *args):
        self.prost.move_ip(self.px_v, self.py_v)
        if self.prost.right >= o_szer or self.prost.left <= 0:
            self.px_v *= -1
        if self.prost.top <= 0 or self.prost.bottom >= o_wys:
            self.prost.x = (o_szer - 10) / 2
            self.prost.y = (o_wys - 10) / 2
        for pal in args:
            if self.prost.colliderect(pal.prost):
                self.py_v *= -1


class Gracz2():
    def __init__(self, pal, pilka, pal_v=5):
        self.pal = pal
        self.pilka = pilka
        self.pal_v = pal_v

    def ruszaj(self):
        if self.pilka.prost.centerx > self.pal.prost.centerx:
            self.pal.prost.x += self.pal_v
        elif self.pilka.prost.centerx < self.pal.prost.centerx:
            self.pal.prost.x -= self.pal_v


if __name__ == "__main__":
    gra = PongGra(800, 400)
    gra.uruchom()
