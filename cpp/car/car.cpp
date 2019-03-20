
/*
 * car.cpp
 */
#include <iostream>
#include <cstdlib>
#include "car.h"
#include "osoba.h"
using namespace std;
Car::Car() {
    marka=model="";
    rocznik=przebieg=0;
}
Car::Car(string mr, string ml, int r, int p) {
    if (r <= 1990) r = 1990;
    marka = mr;
    model = ml;
    rocznik = r;
    przebieg = p;
}
void Car::dodaj() {
    cout << "Dodaj samochód:"<< endl;
    cout << "Marka: "; cin>>marka;
    cout << "Model: "; cin>>model;
    cout << "Rocznik: "; cin>>rocznik;
    cout << "Przebieg: "; cin>>przebieg;
}
void Car::dane() {
    cout << "\nTwoje piękne auto:"<< endl;
    cout << "Marka: " << marka << endl;
    cout << "Model: " << model << endl;
    cout << "Rocznik: " << rocznik << endl;
    cout << "Przebieg: " << przebieg << endl;
}

void Car::laduj(int)
{
    cout<<"Ile osob chcesz przewiezc: "; cin>>ileosob;
    cout<<endl;
    for(int i=0; i<ileosob; i++)
    {
        Osoba o;
        cout<<"Podaj dane "<<i+1<<" osoby:"<<endl;
        cout<<"Imie: "; cin>>o.imie;
        cout<<"Nazwisko: "; cin>>o.nazwisko;
        cout<<"Wiek: "; cin>>o.wiek;
        cout<<"Plec: "; cin>>o.plec;
        osoby[i]=o;
    }
}

void Car::pasazerowie(int)
{
    cout<<endl;
    for(int i=0; i<ileosob; i++)
    {
        cout<<i+1<<" osoba w samochodzie to: "<<osoby[i].imie<< " " <<osoby[i].nazwisko<<" lat "<<osoby[i].wiek<< ", plec: "<< osoby[i].plec<<endl;
    }
}
