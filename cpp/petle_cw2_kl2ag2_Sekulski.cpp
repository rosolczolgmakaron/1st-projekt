 #include <iostream>
 #include <cmath>

using namespace std;

int main(int argc, char **argv)
{   
    int a, b, c;
    a = b = c = 0;
    
    while(1)
    {       
        cout << "Podaj boki trójkąta."<< endl;
        cout << "Bok a:";
        cin >> a;
        cout << "Bok b:";
        cin >> b;
        cout << "Bok c:";
        cin >> c; 
        cout << "" << endl;
        
        float p = 0.5*(a+b+c);
            
        if(a+b>c && a+c>b && b+c>a)
        {   
            cout <<"Pole trójkąta jest równe:" << sqrt(p*(p-a)*(p-b)*(p-c)) << endl;
            break;
        }
        
    }
    
    return 0;
}
