 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a = 0;
    int b = 0;
    int iloraz=0;
    int wynik=0;
    
   while(b==0)
   {
    cout << "Podaj dzielną: " << endl;
    cout << "Dzielna: ";
    cin >> a;
    cout<< ""<<endl;
    cout << "Podaj dzielnik: " << endl;
    cout << "Dzielnik: ";
    cin >> b;
	}
    
    while(true)
    {
        wynik=a-b;
        
        if(wynik>=0)
        {   
            iloraz++;
            a=0;
            a+=wynik;
        }
        else break;
    }
    
    cout<<"Iloraz jest równy: "<< iloraz;
    
    return 0;
}

