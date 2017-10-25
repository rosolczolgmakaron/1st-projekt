/*
* tabele.cpp
*/

 #include <iostream>
 #include <cmath>

using namespace std;

void pobierz_dane(int tab[], int rozmiar)
{
    cout<< "Podaj " << rozmiar<< " ocen (0-6): "<<endl;

    for(int i=0; i<rozmiar; i++)
    {
        cin>> tab[i];
    }
}

int sumuj(int tab[], int rozmiar)
{
    int suma=0;
    for(int i=0; i<rozmiar; i++)
    {
        suma+=tab[i];
        cout<< tab[i]<<", ";
    }
    return suma;
}

float dziel(int tab[], int rozmiar)
{
    return sumuj(tab, rozmiar)/float(rozmiar);
}

int main(int argc, char **argv)
{
    int rozmiar=0;

    cout<<"Ile ocen?"<<endl;
    cin>> rozmiar;

    int liczby[rozmiar];

    pobierz_dane(liczby, rozmiar);

    cout<<"Podane oceny: ";

    //~for(int i=0; i<rozmiar; i++)
    //~{
        //~suma+=liczby[i];
        //~cout<< liczby[i]<<", ";
    //~}

    cout<<endl<<"Suma ocen: "<< sumuj(liczby, rozmiar)<<endl;
    cout<<"Średnia: "<< dziel(liczby, rozmiar)<<endl;

    return 0;
}
