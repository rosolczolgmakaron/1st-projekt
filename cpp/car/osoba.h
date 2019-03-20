#include <iostream>
#include <cstdlib>

#ifndef __OSOBA_H_
#define __OSOBA_H_

using namespace std;

class Osoba{
    public:
        string imie;
        string nazwisko;
        int wiek = 0;
        string plec;
        Osoba();
        Osoba(string, string, int, string);
};
#endif
