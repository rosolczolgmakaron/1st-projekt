
/*
 * zad_zlozonosc.cpp
 */


#include <iostream>

using namespace std;

void wypisz_nieparzyste(int n)
{
    for(int i=1;i<=n;i+=2)
    {
        cout<<i<<endl;
    }
}

int main(int argc, char **argv)
{
    int n=0;
    cout<<"Podaj wartosc liczby n:";
    cin>>n;
    
    wypisz_nieparzyste(n);
    
    return 0;
}
