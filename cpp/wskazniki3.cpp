/*
 * wskazniki.cpp
 */

#include <iostream>
using namespace std;

struct uczen {
    char imie[10];
    float srednia;
};
int main(int argc, char **argv)
{
    uczen tab[2];
    uczen *wsk;
    wsk = tab;
    for(int i=0; i <2; i++){
        cout << "Imię: " << endl;
        cin >> wsk->imie;
        cout << "Średnia: " << endl;
    }
    return 0;
}
