/*
 * dec2bin.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    char znakA = 'A';
    char znakB = 'B';
    int l14 = 14;
    int l15 = 15;
    
    cout << (int)znakA << (int)znakB << endl;
    cout << (char)l14 << (char)l15 << endl;
	int liczba = 0;
    int podstawa = 0;
    int reszty[16];
    int i =0;
    
    cout << "Podaj liczbę i podstawę: ";
    cin >> liczba >> podstawa;
    do{
        reszty[i] =  liczba%podstawa;
        liczba = liczba / podstawa;
        i++;
    } while(liczba>0);
    
    //~for (int j = i - 1; j >= 0; j--){
        //~cout << reszty[j];
    //~}
    
    while(i-1 >= 0){
        i--;

        cout << reszty[i];
    }
	return 0;
}

