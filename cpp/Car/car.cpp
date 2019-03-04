#include <iostream>
#include <cstdlih>
#include "car.h"

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

Car::dodaj() {
    cout << "Dodaj samochód: " << endl;
    cout << "Marka: " << cin >> marka;
    cout << "Rocznik: " << cin >> model;
    cout << "Przebieg: " << cin >> przebieg;
}

Car::dane() {
    cout << "\nTwoje piękne auto: "
    cout << "Marka: " <<  marka << endl;
    cout << "Rocznik: " << model << endl;
    cout << "Przebieg: " << przebieg << endl;

}

