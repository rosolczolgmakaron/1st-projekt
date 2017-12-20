/*
/  ciag.cpp
*/

#include <iostream>
using namespace std;


int wartosc (int a)
{
    if (a==1)
    {
        return 1;
    }
    else if (a==2)
    {
        return 2;
    }
    else
    {
        return wartosc();
    }
}

int main(int argc, const char * argv[]) {

    int n;
    cout << "Podaj numer wyrazu ciagu: ";
    cin >> n;
    cout << "Wartosc tego wyrazu: " << wartosc(n);

    cin.ignore();
    getchar();
    return 0;
}
