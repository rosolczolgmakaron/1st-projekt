/*
/  main.cpp
/  C++
*/

#include <iostream>
using namespace std;


int wartosc (int n)
{
    if (n==1) {
        return 1;
    } else {
        return wartosc((n-1)+(2*n)+(n-2));
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
