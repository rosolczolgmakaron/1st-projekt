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
        pygame.display.set_caption('Pong')

    def rysuj(self):
        """ Rysowanie okna gry """
        # kolor okna gry, składowe RGB podane w tupli
        self.pow.fill((200, 255, 255))
        pygame.display.update()


class PongGra(object):
    """ Kontroler gry """

    def __init__(self, szer, wys):
        pygame.init()
        self.plansza = Plansza(szer, wys)

    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.plansza.rysuj()


if __name__ == "__main__":
    gra = PongGra(800, 400)
    gra.uruchom()
