/*
 * Sekulski_ulamek.cpp
 * Funkcja skraca ułamek podany w postaci pary liczb
 */


#include <iostream>
using namespace std;


int nwd(int a, int b)
{
    while(a>0)
    {
        a %= b;
        b -= a;
    }
    return b;
}

int main(int argc, char **argv)
{
	int a = 0; // licznik
    int b = 0; // mianownik
    
    cout<<"Podaj licznik: ";
    cin>> a;
    cout<<"Podaj mianownik: ";
    cin>> b;
    
    cout<<"Ułamek wynosi: "<< a/(nwd(a, b)) <<"/"<< b/(nwd(a, b)) <<endl;
    
	return 0;
}

