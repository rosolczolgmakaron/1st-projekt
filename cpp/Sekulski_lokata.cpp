/*
 * Sekulski_lokata.cpp
 * Funkcja liczy stan konta pana Nowaka po n miesiącach oraz kwotę ostatniej wpłaty.
 */


#include <iostream>
using namespace std;

void kwota(int n)
{
    int a = 0; // ilość pieniędzy na lokacie
    int b = 100; // wysokość wpłaty
    int c = 0; // wysokosc ostatniej wpłaty
    
    for(int i=0; i<=n; i++)
    {
        a += b;
        b += 10;
    }
    
    c = 100+(n*10);
    
    cout<<"Ilosć pieniędzy na lokacie po "<<n<<" miesiącach: "<<a<<endl;
    cout<<"Wysokość ostatniej wpłaty: "<<c<<endl;
}
int main(int argc, char **argv)
{
	int n = 0;
    do
    {
        cout<<"Podaj ilosc miesięcy: ";
        cin>>n;
    }while(n<0);
    
    kwota(n);
    
	return 0;
}

