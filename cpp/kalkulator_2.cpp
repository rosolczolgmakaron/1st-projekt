/*
 * kalkulator
 */
 
 
 #include <iostream>

using namespace std;

int sumuj(int a, int b)
{
    int wynik = a + b;
    return wynik;
}


int odejmij(int a, int b)
{
    int wynik = a - b;
    return wynik;
}


int mnoz(int a, int b)
{
    int wynik = a * b;
    return wynik;
}


int dziel(int a, int b)
{
    float wynik = a / b;
    return wynik;
}


int main(int argc, char **argv)
{
    
    int a, b;
    a = b = 0;
    cout << "Podaj 1. liczbę: ";
    cin >> a;
    cout << "Podaj 2. liczbę: ";
    cin >> b;
    
    cout << endl << "Suma: " << sumuj(a, b) << endl;
    cout << "Różnica: " << odejmij(a, b) << endl;
    cout << "Iloczyn: " << mnoz(a, b) << endl;
    cout << "Iloraz: " << dziel(a, b) << endl;
    
    return 0;
}
