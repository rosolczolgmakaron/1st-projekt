/*
 * tablica_3kl.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int liczby[20];
    srand(time(NULL)); //inicjacja generatora liczb losowych
    for (int i = 0; i < 20; i++)
    {
        liczby[i] = rand() % 100; //zapis liczb do tablicy
    }

    for (int i = 0; i < 20; i++)
    {
        cout << liczby[i] << " ";
    }
    if (i % 2 = 0)
    {
        cout << "Parzysta";
    }
    else
    cout << "Nieparzysta";
	return 0;
}
