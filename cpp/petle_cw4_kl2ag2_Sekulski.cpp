 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int x = 0;
    int wynik = 0;
    
    cout << "Podaj liczbę: " << endl;
    cin >> x ;
    
    while(x>0)
    {
        wynik += x%10;
        x /= 10;
    }
    
    cout << "Suma: "<< wynik << endl;
    cout<< "" << endl;

    return 0;
}
