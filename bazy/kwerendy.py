#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3


def kwerenda1(cur):
    cur.execute("""
        SELECT klasa, ocena, przedmiot, AVG(ocena) AS srednia FROM oceny
        INNER JOIN uczniowie ON uczniowie.id=oceny.id_uczen
        INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
        INNER JOIN przedmioty ON przedmioty.id=oceny.id_przedmiot
        WHERE przedmiot = 'matematyka'
        GROUP BY klasy.id
        ORDER BY srednia DESC

    """)
    # SELECT klasa, przedmiot, ocena, AVG(ocena) AS srednia FROM przedmioty
    # INNER JOIN oceny ON przedmioty.id=oceny.id_przedmiot
    # INNER JOIN klasY ON uczniowie.id_klasa=klasy.id
    # GROUP BY id_przedmiot
    # ORDER BY srednia DESC

    # SELECT klasa, AVG(ocena) AS srednia FROM oceny
    # INNER JOIN uczniowie ON uczniowie.id=oceny.id_uczen
    # INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
    # GROUP BY klasy.id
    # ORDER BY srednia DESC

    # WITH srednie AS (
    # SELECT nazwisko, imie, AVG(ocena) AS srednia FROM uczniowie
    # INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
    # GROUP BY uczniowie.id
    #) SELECT COUNT(srednia) FROM srednie
    # WHERE srednia > 3.8

    # SELECT klasa, COUNT(uczniowie.id) AS ilosc FROM uczniowie
    # INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
    # GROUP BY klasa
    # ORDER BY ilosc DESC

    # SELECT nazwisko, imie, klasa FROM uczniowie
    # INNER JOIN klasy ON uczniowie.id_klasa=klasy.id

    # SELECT COUNT(id) FROM uczniowie
    # WHERE egz_mat > (SELECT AVG(egz_mat) FROM uczniowie)
    # GROUP BY plec

    # SELECT plec, AVG(egz_mat), AVG(egz_hum), AVG(egz_jez) FROM uczniowie GROUP BY plec
    # COUNT(id) FROM uczniowie
    # WHERE egz_hum > 40 AND egz_hum > 40
    # ORDER BY egz_mat DESC
    # LIMIT 5

    # SELECT * FROM nazwiska WHERE imie1 LIKE 'A__a'
    # SELECT * FROM nazwiska WHERE nazwisko LIKE 'G%'
    # SELECT COUNT(*) FROM nazwiska WHERE imie1 LIKE 'A__a'
    # SELECT COUNT(*) FROM nazwiska INNER JOIN dane_osobowe ON nazwiska.nr_ucznia = dane_osobowe.nr_ucznia
    # WHERE miejsce_urodz='Gdańsku'
    # WHERE miejsce_urodz <> 'Gdańsku'
    # WHERE miesiac = 7 OR miesiac = 8

    for row in cur.fetchall():
        print(tuple(row))


def main(args):
    # KONFIGURACJA #####################
    baza = 'uczniowie'
    tabele = ['nazwiska', 'dane_osobowe', 'oceny']
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
