/*
 * pętle
 */
 
 
 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int suma = 0; //suma kolejnych liczb
    int liczba = 0; //liczba wprowadzana

    while(suma<=100) //pętla nieskończona
    {
        cout << "Podaj liczbe: " << endl;
        cin >> liczba ;
        suma += liczba;
        cout << "Suma: "<< suma << endl;
        cout<< "" << endl;
    }

    return 0;
}
