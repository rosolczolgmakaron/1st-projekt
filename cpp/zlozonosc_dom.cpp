#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int n = 0;
    int i = 2;
    do
    {
        cout<<"Podaj liczbe: ";
        cin>>n;
    }while(n<2);
    
    while(i*i <= n)
    {
        if(n%i == 0)
        {
            cout<<n<<" jest liczbą złożoną"<<endl;
            return 0;
        }
        i++;
    }
    cout<<n<<" jest liczbą pierwszą"<<endl;
    return 0;
}
