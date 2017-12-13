/*
 * ciag_fibonacciego.cpp
 */


#include <iostream>

using namespace std;

int fib_iter(int n)
{
	if ( n == 0)
		return 0;
	else if ( n == 1)
		return 1;
	int a = 0;
	int b = 1;
	int tmp;
	cout << a << endl;
	for (int i = 1 ; i < n; i++) 
	{	tmp = b;
		b = a + b;
		a = tmp;
	}
    cout << a << " " << b << " " << b / a << endl;
    return b;
}


int main(int argc, char **argv)
{
	int n;
	cout << "Numer wyrazu ciągu: " << endl;
	cin >> n;
	printf("Wyraz %d = %d", n, fib_rek(n));	
	return 0;
}
