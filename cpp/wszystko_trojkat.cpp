#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char **argv)
{
    int a, b, c;
    a = b = c = 0;
    float x, y, z, p;
    x = y = z = p = 0;
    
    cout << "Podaj 3 boki trójkąta." << endl;
    cout << "Bok a:";
    cin >> a;
    cout << "Bok b:";
    cin >> b;
    cout << "Bok c:";
    cin >> c; 
    
    x= (b*b+c*c-a*a);
    y= (c*c+a*a-b*b);
    z= (a*a+b*b-c*c);
    p = (a+b+c)/2;
    
    if (a+b>c && a+c>b && b+c>a)
    {
    cout << "" << endl;
    cout << "Obwód trójkąta jest równy:" << a+b+c << endl;
    cout << "Pole trójkąta jest równe:" << sqrt(p*(p-a)*(p-b)*(p-c)) << endl;
    cout << "" << endl;
    cout << "Wysokość padająca na bok a ma długość:" << 2*sqrt(p*(p-a)*(p-b)*(p-c))/a << endl;
    cout << "Wysokość padająca na bok b ma długość:" << 2*sqrt(p*(p-a)*(p-b)*(p-c))/b << endl;
    cout << "Wysokość padająca na bok c ma długość:" << 2*sqrt(p*(p-a)*(p-b)*(p-c))/c << endl;
    cout << "" << endl;
    cout << "Kąt na przeciwko boku a:" << 180*(acos(x/(2*b*c))/M_PI) << "∘" << endl;
    cout << "Kąt na przeciwko boku b:" << 180*(acos(y/(2*a*c))/M_PI) << "∘" << endl;
    cout << "Kąt na przeciwko boku c:" << 180*(acos(z/(2*a*b))/M_PI) << "∘" << endl;
    }
    
    else
    {
    cout << "Błąd!" << endl;
    }
    
    if (a+b<c || a+c<b || b+c<a)
    {
    cout << "Z podanych boków nie można zbudować trójkąta." << endl;
    }
    
    
    
    return 0;
}
