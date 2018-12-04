#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# nazwa pliku bazy
baza_nazwa = 'todo.db'
# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///' + baza_nazwa)  # ':memory:'
# jeżeli brak tabel w bazie, zostaną utworzone
if not baza.dialect.has_table(baza, "osoba"):
    BazaModel.metadata.create_all(baza)
# tworzymy sesję, która przechowuje obiekty i umożliwia "rozmowę" z bazą
BDSesja = sessionmaker(bind=baza)
sesja = BDSesja()


def ladujDane(sesja):
    """ Przygotowanie początkowych danych testowych """
    if sesja.query(Osoba).count() > 0:
        return
    osoby = ('adam', 'ewa')
    zadania = ('Pierwsze zadanie', 'Drugie zadanie', 'Trzecie zadanie')
    for login in osoby:
        o = Osoba(login=login, haslo='123')
        sesja.add(o)
        for tresc in zadania:
            sesja.add(Zadanie(tresc=tresc, osoba=o))
    sesja.commit()


def dodajZadanie(sesja, osoba, tresc):
    """ Dodawanie nowego zadania """
    zadanie = Zadanie(tresc=tresc, osoba=osoba)
    sesja.add(zadanie)
    sesja.commit()
    return [
        zadanie.id,
        zadanie.tresc,
        '{0:%Y-%m-%d %H:%M:%S}'.format(zadanie.datad),
        zadanie.wykonane,
        False]


def pobierzDane(sesja, osoba):
    zadania = []
    wpisy = sesja.query(Zadanie).filter(Zadanie.osoba == osoba)
    for z in wpisy:
        zadania.append([
            z.id,
            z.tresc,
            '{0:%Y-%m-%d %H:%M:%S}'.format(z.datad),
            z.wykonane,
            False
        ])
    return zadania


def loguj(sesja, login, haslo):
    osoba = sesja.query(Osoba).filter(Osoba.login == login,
                                      Osoba.haslo == haslo).one_or_none()
    if not osoba:
        osoba = sesja.query(Osoba).filter(Osoba.login == login).first()
        if not osoba:
            osoba = Osoba(login=login, haslo=haslo)
            sesja.add(osoba)
            sesja.commit()
        else:
            osoba = None

    return osoba


def zapiszDane(sesja, zadania):
    """ Zapisywanie zmian """
    for i, z in enumerate(zadania):
        # utworzenie instancji zadania
        zadanie = sesja.query(Zadanie).filter(Zadanie.id == z[0]).one()
        if z[4]:  # jeżeli zaznaczono zadanie do usunięcia
            sesja.delete(zadanie)  # usunięcie zadania z bazy
            del zadania[i]  # usunięcie zadania z danych modelu
        else:
            zadanie.tresc = z[1]
            zadanie.wykonane = z[3]
            sesja.commit()


def main(args):
    ladujDane(sesja)
    osoba = loguj(sesja, 'ewa', '123')
    if osoba:
        print(osoba.login, osoba.id)
    else:
        print("Błędne hasło!")
    # osoba = loguj(sesja, 'ola', '12')
    # if osoba:
    #     print(osoba.login, osoba.id)
    # else:
    #     print("Błędne hasło!")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
