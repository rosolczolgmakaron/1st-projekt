/*
 * car.cpp
 */
#include <iostream>
#include <cstdlib>
#include "osoba.h"

using namespace std;

Osoba::Osoba() {
    imie=nazwisko=plec="";
    wiek=0;
}

Osoba::Osoba(string im, string naz, int lat, string pl) {
    imie = im;
    nazwisko = naz;
    wiek = lat;
    plec = pl;
}

