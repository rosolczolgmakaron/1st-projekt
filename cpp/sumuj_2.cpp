/*
 * pętle
 */
 
 
 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int suma = 0; //suma kolejnych liczb
    int liczba = 0; //liczba wprowadzana
    
    for(;;)
    {
        cout << "Podaj liczbę: " << endl;
        cin >> liczba ;
        suma += liczba;

        if (suma >= 100) break;
        {
            cout << "Suma: "<< suma << endl;
            cout<< "" << endl;
        }
    }

    return 0;
}
