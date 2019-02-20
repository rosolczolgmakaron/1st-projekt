/*
 * pliki.cpp
 */

#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <iomanip>

using namespace std;

// tekst.txt
// tekst.bak

float sumuj(char plik[]){
    ifstream wejscie(plik);
    if (!wejscie) { cout << "Błąd otwarcia pliku!"; return 0; }
    
    float liczba = 0;
    float suma = 0;
    while(!wejscie.eof()) {
        wejscie >> liczba;
        suma += liczba;
    }
    wejscie.close();
    cout << "Suma liczb: " << suma << endl;
    return suma;
}

int liczZnaki(char plik[]) {
    ifstream wejscie(plik);
    if (!wejscie) { cout << "Błąd otwarcia pliku!"; return 0; }
    char plik2[15];
    strcpy(plik2, plik);
    char *wsk;
    wsk = strstr(plik2, ".txt");
    strncpy(wsk, ".bak", 4);
    ofstream wyjscie(plik2);
    if (!wyjscie) { cout << "Błąd otwarcia pliku!"; return 0; }
    
    char z; // pojedynczy odczytany znak
    int ile, ileal, ilenum, ilealnum, ilew;
    ile = ileal = ilenum = ilealnum = ilew = 0;
    
    while(!wejscie.eof()) {
        wejscie.get(z);  // odczytanie pojedynczego znaku
        if (wejscie) {
            ile++;
            if (isalpha(z)) ileal++;
            if (isdigit(z)) ilenum++;
            if (isalnum(z)) ilealnum++;
            if ((int)z == 10) ilew++;
        }
    }
    
    wejscie.close(); wyjscie.close();
    cout << setw(10) << "Znaków:" << ile << endl;
    cout << setw(10) << "Liter:" << ileal << endl;
    cout << setw(10) << "Cyfr:" << ilenum << endl;
    cout << setw(10) << "Alfnum:" << ilealnum << endl;
    cout << setw(10) << "Wierszy:" << ilew << endl;
    return ile;
}

void czytajCyfry(char plik[]) {
    ifstream wejscie(plik);
    if (wejscie) {
        string plik2 = "cyfry.txt";
        ofstream wyjscie(plik2);
        char z;
        while(!wejscie.eof()) {
            wejscie.get(z);  // odczytanie pojedynczego znaku
            if (wejscie) {
                if (isdigit(z) || z == '.') wyjscie << z;
                //TODO: wyeliminować zapisywanie pustych wierszy
                //TODO: odczytywanie liczb ujemnych
                if ((int)z == 10) wyjscie << "\n";
            }
        }
        wejscie.close(); wyjscie.close();
    }
}


int main(int argc, char **argv)
{
    char nazwa[15];
    cout << "Podaj nazwę pliku: ";
    cin >> nazwa;
    // liczZnaki(nazwa);
    //sumuj(nazwa);
    czytajCyfry(nazwa);
    char nazwa2[10]="cyfry.txt";
    sumuj(nazwa2);
    return 0;
}

