#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

# inicjacja modułów PyGame
pygame.init()
# przygotowanie okna gry
O_SZER, O_WYS = 800, 400
plansza = pygame.display.set_mode((O_SZER, O_WYS), 0, 32)
# tytuł okna gry
pygame.display.set_caption('Pong')
PAL_SZER, PAL_WYS, MAKS_V = 100, 20, 10

# paletka gracza 1
# utworzenie powierzchni paletki, wypełnienie jej kolorem,
pal1 = pygame.Surface([PAL_SZER, PAL_WYS])
pal1.fill((0, 0, 255))
# ustawienie prostokąta zawierającego paletkę w początkowej pozycji
pal1_prost = pal1.get_rect()
pal1_prost.x = 350
pal1_prost.y = 20

pal2 = pygame.Surface([PAL_SZER, PAL_WYS])
pal2.fill((255, 0, 0))
# ustawienie prostokąta zawierającego paletkę w początkowej pozycji
pal2_prost = pal2.get_rect()
pal2_prost.x = 350
pal2_prost.y = 360

# pal3 = pygame.Surface([20, 100])
# pal3.fill((255, 0, 0))
# # ustawienie prostokąta zawierającego paletkę w początkowej pozycji
# pal3_prost = pal3.get_rect()
# pal3_prost.x = 20
# pal3_prost.y = 150

# pętla główna programu
while True:
    # obsługa zdarzeń
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # kolor okna gry, składowe RGB podane w tupli
    plansza.fill((200, 255, 255))

    # umieść na planszy paletki graczy
    plansza.blit(pal1, pal1_prost)
    plansza.blit(pal2, pal2_prost)
    # plansza.blit(pal3, pal3_prost)

    # rysowanie okna
    pygame.display.update()
