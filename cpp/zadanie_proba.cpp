/*
 * Sekulski_alg2.cpp
 */


#include <iostream>
using namespace std;


void czy_parzysta( int a)
{
    int i = 2;
    
    while(a == i) // while(a!=) //dla warunku (a == i) pętla nie wykona się
    {
        
        if(i==100)
        {
            cout<<"nieparzyste";
        break;
        }
        
        i +=2;
    }
    
    //if(a==i) // brak tego "ifa" sprawia że liczbom parzystym niezwracana jest żadna wartość
    //{
    //    cout<<"parzyste";
    //}
}

int main(int argc, char **argv)
{
	int a = 0;
    do
    {
        cout << "Podaj liczbe: ";
        cin >> a;
    }while(0>=a || a>=100); 
    
    
    czy_parzysta(a);
    
    
	return 0;
}
