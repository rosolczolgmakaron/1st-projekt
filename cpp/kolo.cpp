/*
 * hello.cpp
 */


#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{	
    int r =0; // deklaracja typu całkowitego i inicjacja zmiennej
	cout << "Podaj promień koła: ";
    cin >> r;
    cout << "Pole koła: " << M_PI * r * r << endl;

	return 0; 
}

