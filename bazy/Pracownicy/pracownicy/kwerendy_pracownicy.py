#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3


def kwerenda1(cur):
    cur.execute("""
        SELECT * FROM pracownicy
    """)

    for row in cur.fetchall():
        print(tuple(row))


def main(args):
    # KONFIGURACJA #####################
    baza = 'pracownicy'
    tabele = ['pracownicy', 'kontakty', 'stanowiska', 'place']
    roz = '.txt'
    naglowki = True  # czy pliki źródłowe zawierają nagłówki?
    ####################################
    con = sqlite3.connect(baza + '.db')  # połączenie
    cur = con.cursor()  # obiekt kursora

    kwerenda1(cur)

    con.commit()
    con.close()
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
