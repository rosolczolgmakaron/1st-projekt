/*
 * liczby pierwsze
 */
 
 
#include <iostream>
#include <cstdlib>
using namespace std;
 
bool czy_pierwsza(int n)
{
  if(n<2)
    return false;
 
  for(int i=2;i*i<=n;i++)
    if(n%i==0)
      return false;
  return true;
}
 
int main()
{
  for(int n = 1; n <= 1000; n++ )
 
  if(czy_pierwsza(n))
    cout<<"Liczba "<<n<<endl;
 
  system("pause");
  return 0;
}

