/*
 * petla_2.cpp
 */


#include <iostream>
using namespace std;

    
void zlicz_it(int n)
{
    int a = 0; //liczba
    int parz=0; //parzyste liczby
   
    for(int i=0; i<n;i++)
    {
        cout<<"Podaj "<<i+1<<" liczbe: ";
        cin>>a;
       
        if(a%2 == 0)
            parz++;
    }
    cout<<"Parzystych: "<<parz<<endl;
    cout<<"Nieparzystych: "<<n-parz;
}
 
 
int main(int argc, char **argv)
{
    int n = 0;
   
    while(n<=0)
    {
        cout<<"Ile liczb chcesz podac: ";
        cin>>n;
    }
   
    zlicz_it(n);
   
	return 0;
}

