/*
 * spr_19_01.cpp
 * pierwszy rysunek (i=100)
 */
 
 
#include <iostream>
 
using namespace std;
 
void sprawdz_liczbe(int a)
{
    int i = 2;
    
    while(true)
    {
        if(a==i)
        {
            cout<<"parzyste";
            break;
        }
        else
        {
        i+=2;
        if(i==100)
        {
            cout<<"nieparzyste";
            break;
        }
        }
    }
}
 
int main(int argc, char **argv)
{
    int a = 0;
    do
    {
        cout<<"Podaj liczbe:";
        cin>>a;
    }while(a<=0 || a>=100);
   
   
    sprawdz_liczbe(a);
   
   
    return 0;
}
