/*
 * silnia_2.cpp
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int i, n, silnia;
    cout << "Podaj n: ";
    cin >> n;
    silnia = 1;
    i = 1;
    do {
        silnia *= i;
        i++;
    } while(i <= n);
    cout << n << "! = " << silnia << endl; 
            
	return 0;
}

