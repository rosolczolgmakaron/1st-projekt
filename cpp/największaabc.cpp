/*
 * największa.cpp
 * Pobierz dwie liczby od użytkownika i wydrukuj większą
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int a, b, c;
    a = b = c = 0;
    cout << "Podaj trzy liczby"<< endl;
    cout << "Liczba a:";
    cin >> a;
    cout << "Liczba b:";
    cin >> b;
    cout << "Liczba c:";
    cin >> c;
        if (c < b) 
    {
        if (b > a)
        {
        cout << "Największe b=" << b;
        }
        if (b == a)
        {
        cout << "Największe są a i b równe:" << b;
        }
    } 
        else if (b < a) 
    {
        if (a > c)
        {
        cout << "Największe a=" << a;
        }
        if (a == c)
        {
        cout << "Największe są a i c równe:" << a;
        }
    } 
        else if (a < c)
    {
        if (c > b)
        {
        cout << "Największe c=" << c;
        }
        if (b == c)
        {
        cout << "Największe są b i c równe:" << b;
        }
    }
        else cout << "Liczby a,b,c są równe";
	return 0; 
}

