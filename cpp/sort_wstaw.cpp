#include <iostream>

using namespace std;

void sort_wstaw(int t[], int n)
{
    int el=0;
    int k=0;
    
    for(int i=1;i<n;i++)
    {
        el = t[i];
        k = i-1;
        
        while(k>=0 && t[k] > el)
        {
            t[k+1] = t[k];
            k--;
        }
        t[k+1] = el;
    }
}
void drukuj(int tab[], int n)
{
    for(int i=0; i<n; i++)
    {
        cout<<tab[i]<<" ";
    }
}

int main(int argc, char **argv)
{
    int ile = 8;
    int lista[] = {4, 3, 7, 0, 2, 3, 1, 9};

    drukuj(lista, ile);

    cout<<endl;

    sort_wstaw(lista, ile);
    drukuj(lista, ile);
    
    return 0;
}
