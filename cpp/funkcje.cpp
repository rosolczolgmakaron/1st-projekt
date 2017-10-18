/*
* funkcje.cpp
*/

 #include <iostream>
 #include <cmath>

using namespace std;

void dodaj(int a, int b)
{
    cout<< "Suma: "<< a+b <<endl;
}

int odejmij(int l1, int l2)
{
    return l1-l2;
}

int iloczyn(int x, int y)
{
    return x*y;
}

float iloraz(float s, float t)
{
    if(t==0)
    {
        cout<<"Dzielnik nie może być równy 0"<<endl;
    }
    return 0;
}

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
    
    cout<<"Podaj dwie liczby."<<endl;
    cin>> a >> b;

    dodaj(a,b); // wywołanie funkcji
    
    cout<< "Różnica: " << odejmij(a,b) <<endl;
    cout<< "Iloczyn: " << iloczyn(a,b) <<endl;
    cout<< "Iloraz: " << iloraz(a,b) <<endl;

    return 0;
}
