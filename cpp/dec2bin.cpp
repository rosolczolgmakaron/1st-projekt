/*
 * dec2bin.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    
    char znakA = 'A';
    char znakB = 'B';
    int l14 = 65;
    int l15 = 66;
    cout<< (int)znakA <<(int)znakB <<endl;
    cout<<(char)l14 << (char)l15<<endl;
    
    int n = 0; //120 > 1111000
    int p = 2;
    int reszty[16];
    int i = 0;
    
    cout<<"Podaj liczbe(dec): ";
    cin>>n;
    cout<<"Podaj podstawe: ";
    cin>>p;
    
    do
    {
        reszty[i] = n % p;
        n /= p;
        i++;
    }while(n > 0);
    
    //~ for(int j = i-1; j>=0;j--)
    //~ {
      //~ if(p > 10 && reszty[j]>=10)
        //~ {
            //~ cout<<(char)(reszty[j]+55);
        //~ }
        //~ else
        //~ {
            //~ cout<<reszty[j];
        //~ }
    //~ }
    
    //i--;
    while(i-1>=0)
    {
        i--;
        if(p > 10 && reszty[i]>=10)
        {
            cout<< (char)(reszty[i]+55);
        }
        else
        {
            cout<<reszty[i];
        }
    }

    return 0;
}
