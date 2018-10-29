#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza.py
import csv
import sqlite3
import os.path

def czy_jest(plik):
    """F. sprawdza, czy plik istnieje na dysku"""
    if not os.path.isfile(plik):
        print("Plik {} nie istnieje!".format(plik))
        return False
    return True

def czytaj_dane(plik, separator=","):
    dane = []  # pusta lista na rekordy
    
    if not czy_jest(plik):
        return dane
    
    with open(plik, 'r', newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator)
        for rekord in tresc:
            dane.append(rekord)
    return dane


def ile_kolumn(cur, tab):
    """F. liczy i zwraca liczbę kolumn w podanej tabeli"""
    licznik = 0
    for kol in cur.execute("PRAGMA table_info('" + tab + "')"):
        licznik += 1
    return licznik

def main(args):
    # KONFIGURACJA #####################
    baza = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    roz = '.csv'
    naglowki = False  # czy pliki źródłowe zawierają nagłówki?
    ####################################
    con = sqlite3.connect(baza + '.db')  # połączenie
    cur = con.cursor()  # obiekt kursora

    if not czy_jest(baza + '.sql'):
        return 0

    with open(baza + '.sql', 'r') as plik:
        cur.executescript(plik.read())

    for tab in tabele:
        ile = ile_kolumn(cur, tab)
        dane = czytaj_dane(tab + roz, separator=',')
        ile_d = len(dane[0])
        if ile > ile_d:
            dane2 = []  # lista pomocnicza
            for r in dane:
                r.insert(0, None)
                dane2.append(r)
            dane = dane2
        ile = len(dane[0])
        if naglowki:
            dane.pop(0)  # usunięcie rekordu z nagłówkami
        
        cur.executemany('INSERT INTO ' + tab + ' VALUES('+ ','.join(['?']*ile) +')', dane)
        
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
