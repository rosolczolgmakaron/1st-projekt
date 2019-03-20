
/*
 * samochod.cpp
 */
#include <iostream>
#include <cstdlib>
#include "car.h"
#include "osoba.h"
using namespace std;

int main(int argc, char **argv)
{
    Car s2 = Car();
    int ile = 2;
    s2.dodaj();
    s2.dane();
    s2.laduj(ile);
    s2.pasazerowie(ile);
	return 0;
}
