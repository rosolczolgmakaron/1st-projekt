/*

 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	float masa=0;
    float wzrost=0;
    float bmi=0;
    
    while (1)
    {
        cout << "Podaj swoją masę: ";
        cin >> masa;
        cout << "Podaj swój wzrost w centymetrach: ";
        cin >> wzrost;
        bmi=masa/(wzrost*wzrost)*10000;
    
        if (18.5 > bmi)
        {
            cout << "niedowaga";
        }
        if (18.5 <=bmi && bmi<24.9)
        {
            cout << "norma";
        }
        if (25<=bmi && bmi<30)
        {
            cout << "nadwaga";
        }
        if (30<=bmi)
        {
            cout << "otyłośc";
        }
    break;
}
	return 0;
}

