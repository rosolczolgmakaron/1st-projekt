/*
 * kalkulator
 */
 
 
 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    char znak;
    
    int a, b;
    a = b = 0;
    
    cout << "Podaj działanie." << endl;
    //cout << "Liczba a:";
    cin >> a;
    //cout << "znak: ";
    cin >> znak;
    //cout << "Liczba b:";
    cin >> b;
    
    cout << "=";
    
    if (znak == '+')
    {
        cout << a+b << endl;
    }
    
    if (znak == '-')
    {
        cout << a-b << endl;
    }
    
    if (znak == '*')
    {
        cout << a*b << endl;
    }
    
    if (znak == '/')
    {
        cout << a/b << endl;
    }
    
    return 0;
}
