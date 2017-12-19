#include <iostream>
using namespace std;

int a(int n)
{
	if (n==1)
	return 1;
	else
	return a(n-1)+(2*n)+(n-2);
}

int main()
{
	int n;
	cout<<"Podaj numer wyrazu: ";
	cin>> n;
	cout<<"Wartość wyrazu: " << a(n);

}
