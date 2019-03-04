/*
 * pliki.cpp
 */

#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <iomanip>

using namespace std;


int liczSamogloski(char plik[]) {
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
    int a, e, i, o, u, y, ileal;
    a = e = i = o = u = y = ileal = 0;
    
    while(!wejscie.eof()) {
        wejscie.get(z);  // odczytanie pojedynczego znaku
        if (int(z)==65 || int(z)==97) a++;
        if (int(z)==69 || int(z)==101) e++;
        if (int(z)==73 || int(z)==105) i++;
        if (int(z)==79 || int(z)==111) o++;
        if (int(z)==85 || int(z)==117) u++;
        if (int(z)==89 || int(z)==121) y++;
        ileal = a + e + i + o + u + y;
        }

    wejscie.close(); wyjscie.close();
    cout << setw(10) << "Samogłosek a jest:" << a << endl;
    cout << setw(10) << "Samogłosek e jest:" << e << endl;
    cout << setw(10) << "Samogłosek i jest:" << i << endl;
    cout << setw(10) << "Samogłosek o jest:" << o << endl;
    cout << setw(10) << "Samogłosek u jest:" << u << endl;
    cout << setw(10) << "Samogłosek y jest:" << y << endl;
    cout << setw(10) << "Samogłosek w sumie jest:" << ileal << endl;
    return ileal;
}

void sort_wstaw(int t[], int n)
{
    int el=0;
    int k=0;
    
    for(int i=1;i<n;i++)
    {
        el = t[i];
        k = i-1;
        
        while(k>=0 && t[k] > el)
        {
            t[k+1] = t[k];
            k--;
        }
        t[k+1] = el;
    }
}

void drukuj(int tab[], int n)
{
    for(int i=0; i<n; i++)
    {
        cout<<tab[i]<<" ";
    }
}

int main(int argc, char **argv)
{
    char nazwa[15];
    cout << "Podaj nazwę pliku: ";
    cin >> nazwa;
    liczSamogloski(nazwa);
    //~ int ile = 6;
    //~ int lista[] = {a, e, i, o, u, y};
    //~ drukuj(lista,ile);
    //~ cout << endl;
    //~ sort_wstaw(lista, ile);
    //~ drukuj(lista, ile);
    return 0;
}

