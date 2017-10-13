 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int n = 0;
    int x = 0;
    int wynik = 0;
    
    cout << "Podaj n: " << endl;
    cout << "n=";
    cin >> n ;
    
    while(n>0)
    {
        x += n%10;
        n /= 10;
    }
    cout << "Suma (1): "<< x <<endl;
    while(x>0)
    {
        wynik += x%10;
        x /= 10;
    }
    cout << "Suma (2): "<< wynik << endl;
    cout<< "" << endl;

    return 0;
}
