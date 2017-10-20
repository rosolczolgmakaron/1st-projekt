/*
* funkcje.cpp
*/

 #include <iostream>
 #include <cmath>

using namespace std;

//int liczba=0; //zmienne globalne
//int krok=0; //zmienne globalne

//void zwieksz1()
//{
    //liczba+=krok;
//}

void zwieksz2(int liczba, int krok) //przekazywanie przez wartość
{
    cout<<&liczba<<" "<< &krok<<endl;
    liczba+=krok;
    cout<<"Liczba po zwiekszeniu: "<<liczba<<endl;
}

void zwieksz3(int &liczba, int &krok) //przekazywanie przez wartość
{
    liczba+=krok;
    cout<<"Liczba po zwiekszeniu: "<<liczba<<endl;
}

int main(int argc, char **argv)
{
    int liczba, krok; //zmienne lokalne
    liczba=krok=0;
    
    cout<<"Popdaj liczbę i krok."<<endl;
    cin>>liczba>>krok;

    cout<<&liczba<<" "<< &krok<<endl;

    zwieksz2(liczba, krok);
    zwieksz2(liczba, krok);
    zwieksz2(liczba, krok);

    cout<<"Liczba po zwiekszeniu: "<<liczba<<endl;
    cout<<"Krok: "<< krok<<endl;

    return 0;
}

