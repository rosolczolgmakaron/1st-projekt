/*
 * binarne.cpp
 */


#include <iostream>

using namespace std;

int wyszukaj_liniowo(int lista[], int el, int n)
{
    for(int i = 0; i < n; i++)
    {
        if (lista[i] == el)
        {
            cout << "Liczba znajduje się na miejscu: ";
            return i;
        }
    }
    return -1;
}

int main(int argc, char **argv)
{
    int ile = 9;
    int tab[ile] = {4, 3, 7, 0, 2, 3, 1, 9, -4};
    int el;
    cout << "Jakiej liczby szukasz?" << endl;
    cin >> el;
    
    cout<<wyszukaj_liniowo(tab, el, ile);
	return 0;
}

