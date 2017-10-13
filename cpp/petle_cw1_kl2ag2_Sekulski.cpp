 /*
 * pętle
 */
 
 
 #include <iostream>
 #include <cmath>

using namespace std;

int main(int argc, char **argv)
{   
    int x=0;
    while(1)
    {   
        cout << "Podaj liczbę."<< endl;
        cin >> x;
        cout << "" << endl;
        
        if (x>0)
        {
            cout << "Kwadrat wprowadzonej liczby: " << x*x << endl;
            cout << "Pierwiastek wprowadzonej liczby: " << sqrt(x) << endl;
            break;
        } 

    }
    
    return 0;
}
