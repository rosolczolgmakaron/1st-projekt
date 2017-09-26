/*
 * największa.cpp
 * Pobierz dwie liczby od użytkownika i wydrukuj większą
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int a, b;
    a = b = 0;
    cout << "Podaj dwie liczby:" << endl;
    cout << "Liczba a:";
    cin >> a;
    cout << "Liczba b:";
    cin >> b;
        if (a < b) 
    {
        cout << "Większe b=" ;
        cout << b;
    } 
        else if (b < a) 
    {
        cout << "Większe a=" ;
        cout << a;
    } 
        else //if (a == b)
    {
        cout << "a równe b" ;
    }
	return 0; 
}

