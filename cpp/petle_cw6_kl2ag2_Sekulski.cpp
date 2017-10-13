 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a = 0;
    int b = 0;
    
    cout << "Podaj dzielną: " << endl;
    cout << "Dzielna: ";
    cin >> a;
    cout<< ""<<endl;
    cout << "Podaj dzielnik: " << endl;
    cout << "Dzielnik: ";
    cin >> b;
    cout<< ""<<endl;
    
    if(b!=0)
    {
        for(a=a-b; a>=0; a-=b)
        {   
            cout<< "Liczba a jest równa: "<< a<< endl;
        }
    }
    
    return 0;
}
