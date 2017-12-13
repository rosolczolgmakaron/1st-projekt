#include <iostream>
#include <cstdlib>
 
using namespace std;
 

 int silnia_rek(int n)
{
	if (n < 2)
		return 1;
	return n * silnia_rek(n - 1) ;
}


int main()
{
    int a;
 
    cout << "podaj liczbe" << endl;
    cin >> a;
 
    cout << "silnia: "<< silnia_rek(a) << endl;
 
    system("PAUSE");
    return(0);
}
