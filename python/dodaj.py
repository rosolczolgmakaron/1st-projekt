#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sumuj(x,y):
    return x+y
    
def odejmij(x,y):
    return x-y

a = int(input("Podaj liczbę.\n"))
b = int(input("Podaj liczbę.\n"))

print("Suma: ", sumuj(a,b))
print("Różnica: ", odejmij(a,b))
