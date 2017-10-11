/*
 * pętle
 */
 
 
 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{   
    int a;
    int i; //zmienna interacyjna
    int suma = 0; //suma kolejnych liczb
    int liczba = 0; //liczba wprowadzana
    
    cout<< "Ile liczb podasz?"<< endl;
    cin >> a;
    cout << "" << endl;
    
    for(i = 1; i <= a; i++ )
    {
        cout << "Podaj liczbę: " << endl;
        cin >> liczba ;
        suma += liczba;
        cout << "Suma: "<< suma << endl;
        cout<< "" << endl;
    }

    return 0;
}
