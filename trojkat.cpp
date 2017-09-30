#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char **argv)
{
    int a, b, c;
    float p = 0;
    a = b = c = 0;
    cout << "Podaj 3 boki trójkąta." << endl;
    cout << "Bok a:";
    cin >> a;
    cout << "Bok b:";
    cin >> b;
    cout << "Bok c:";
    cin >> c; 
    p = (a+b+c)/2;
    
    if (a+b>c && a+c>b && b+c>a)
    {
    cout << "Obwód trójkąta jest równy:" << a+b+c << endl;
    cout << "Pole trójkąta jest równe:" << sqrt(p*(p-a)*(p-b)*(p-c)) << endl;
    }
    
    return 0;
}
