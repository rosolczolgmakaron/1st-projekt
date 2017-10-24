/*
* tabele.cpp
*/

 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int rozmiar=0;

    cout<<"Ile ocen?"<<endl;
    cin>> rozmiar;

    int liczby[rozmiar];
    int suma=0;

    cout<< "Podaj " << rozmiar<< " ocen (0-6): "<<endl;

    for(int i=0; i<rozmiar; i++)
    {
        cin>> liczby[i];
    }

    cout<<"Podane oceny: ";

    for(int i=0; i<rozmiar; i++)
    {
        suma+=liczby[i];
        cout<< liczby[i]<<", ";
    }

    cout<<endl<<"Suma ocen: "<< suma<<endl;
    cout<<"Średnia: "<< float(suma)/float(rozmiar)<<endl;

    return 0;
}
