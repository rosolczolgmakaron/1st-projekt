#include <iostream>
#include <cstdlih>
#include <string>

#ifndef __CAR_H_
#definr __CAR_H_
class Car{
    private:
        string marka;
        string model;
        int rocznik;
        int przebieg;
    public:
        Car();
        Car(string, string, int, int);
        void dodaj();
    }
