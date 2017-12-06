/*
 * Sekulski_dzielniki.cpp
 * Funkcja liczy ilość dzielników liczb całkowitych
 */


#include <iostream>

using namespace std;

int zlicz(int a)
{
    int b = 0; // ilość dzielników
    for(int i=1; i<=abs(a);i++)
    {
        if(a%i == 0)
        {
            b++;
        }
    }
    return b;
}

int main(int argc, char **argv)
{
    int n = 0; // Liczba, dla której sprawdzamy ilość dzielników
    
    cout<<"Podaj liczbe: ";
    cin>>n;
    
    cout<<"Ilosc dzielnikow liczby "<<n<<" jest rowna: "<<zlicz(n);
    return 0;
}

