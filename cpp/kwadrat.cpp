/*
 * hello.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{	
    int bok =0; // deklaracja typu całkowitego i inicjacja zmiennej
	cout << "Podaj bok kwadratu: ";
    cin >> bok;
    cout << "Obwód kwadratu: " << 4 * bok << endl;
    cout << "Pole kwadratu: " << bok * bok << endl;
    
	return 0; 
}

