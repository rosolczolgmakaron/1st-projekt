#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	double Y;
	cout << "Podaj wartosc dla funkcji asin"<< endl;
	cin >> Y;
	double radian = M_PI/180;
	cout << "Arcus sinus w stopniach dla wartości " << Y << " wynosi " << asin(Y)/radian;
	return 0;
}

