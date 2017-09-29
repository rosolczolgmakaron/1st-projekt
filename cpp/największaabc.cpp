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
        
        if (c < b && a<b) 
    {
        cout << "Największe b=" << b;
    }
        else if (c<a && a==b)
    {
        cout << "Największe są a i b równe:" << b;
    }
        else if (b < a && c<a) 
    {
        cout << "Największe a=" << a;
    }
        else if (b< a &&a == c)
    {
        cout << "Największe są a i c równe:" << a;
    }
        else if (a < c && b<c)
    {
        cout << "Największe c=" << c;
    }
        else if (a<b && b == c)
    {
        cout << "Największe są b i c równe:" << b;
    }
        else if (a ==b && b==c)
    {
        cout << "Liczby a,b,c są równe i wynoszą:" << a;
    }
    
	return 0; 
}

