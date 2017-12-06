/*
 * petla_1.cpp
 */


#include <iostream>
using namespace std;

int ilo_it(int a, int iloczyn = 1)
{   
    int n;
    
    cout<< "Podaj ilość liczb: ";
    cin>> n;
    
    for (int i=1; i < n+1; i++)
    {
        cout<< "Podaj liczbę: ";
        cin>> a;
        iloczyn *= a;
    }
    return iloczyn;
}

int main(int argc, char **argv)
{
    int a = 0;
    int iloczyn = 1;
    
    cout<< ilo_it(a, iloczyn);
	return 0;
}

