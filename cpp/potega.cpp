/*
 * potega.cpp
 * 
 * a0 = 1
 * a1 = a
 * an = a * ... * a (n-czynników) dla n zaw. N+ - {1}
 */


#include <iostream>

using namespace std;


int potega_rek(int x, int n)
{    
    if (x == 0)
        return 0;
    else if (n == 0)
        return 1;
    return potega_rek(x, n - 1) * x;
}

int main(int argc, char **argv)
{
    int n;
    float x;
    cout << "Podaj podstawe potęgi: " << endl;
    cin >> x;
    cout << "Podaj wykładnik potęgi: " << endl;
    cin >> n;
    cout << "Wynik: " << potega_rek(x, n) <<endl;
	return 0;
}
