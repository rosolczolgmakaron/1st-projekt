#include <iostream>
#include <math.h>
using namespace std;

class Wektor {
    private:
        double x;
        double y;
    public:
        void pobierz(int);
        void wypisz();
        void dlugosc();
        friend Wektor dodaj(Wektor, Wektor);
        friend Wektor iloczyn_sk(Wektor, Wektor);
        
};

void Wektor::pobierz(int nr) {
    cout << "Podaj współrzędne "<< nr <<  " wektora: " << endl;
    cin >> x;
    cin >> y;
}

void Wektor::wypisz() {
    cout << "[" << x << "," << y << "]" << endl;
}

void Wektor::dlugosc() {
    float a = 0;
    a = sqrt((x*x)+((y*y)));
    cout << "Długość wektora: " << a;
}

Wektor dodaj(Wektor w1, Wektor w2) {
    Wektor w3;
    w3.x = w1.x + w2.x;
    w3.y = w1.y + w2.y;
    return w3;
}

Wektor iloczyn_sk(Wektor w1, Wektor w2) {
    Wektor w4;
    float wsp;
    cout << "Podaj współczynnik skalarny: ";
    cin >> wsp;
    w4.x = w1.x * w2.x * wsp;
    w4.y = w1.y * w2.y * wsp;
    return w4;
}

int main(int argc, char **argv)
{
    Wektor w1;
    w1.pobierz(1);
    w1.wypisz();
    Wektor w2;
    w2.pobierz(2);
    w2.wypisz();
    Wektor w3;
    w3 = dodaj(w1, w2);
    w3.wypisz();
    Wektor w4;
    w4 = iloczyn_sk(w1, w2);
    w4.wypisz();
    w4.dlugosc();
    return 0;
}

