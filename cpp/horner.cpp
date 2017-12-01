/*
 * horner.cpp
 */


#include <iostream>

using namespace std;

// W(x) = 2x^3 + 3x^2 + 5x + 4
// W(x) = x(x^2 + 3x + 5) + 4
// W(x) = x(x(x+3) + 5) + 4

float horner_it(int n, float tab[], float x)
{
    float wynik = tab[0];
    for (int i=1; i < n+1; i++)
    {
        wynik = wynik* x + tab[i];
    }
    return wynik;
}




int main(int argc, char **argv)
{
    float x;
    int n;
    float tab[n];
    
    cout<< "Podaj argument." <<endl;
    cout<< "x=";
    cin>> x;
    cout<< "Podaj stopień wielomianu."<<endl;
    cin>> n; 
    for (int i = 0; i < n; i++)
    {
        cout<< "Podaj współczynniki."<< endl;
        cin>> tab[i];
    }

    cout<< "Wartość wielomianu: " << horner_it(n, tab, x) <<endl;
    
	return 0;
}

