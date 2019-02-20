/*
 * wskazniki.cpp
 */

#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int i = 13;
    float j = 12.09;
    int *wsk1; // deklaracja wskaźnika do liczby całkowitej
    float *wsk2;
    wsk1 = &i;
    wsk2 = &j;
    cout << i << endl;
    cout << wsk1 << endl;
    cout << *wsk1 << endl;
    *wsk1 = (int)*wsk2;
    cout << *wsk1 << endl;
    return 0;
}

