 #include <iostream>
 #include <cmath>

using namespace std;

int main(int argc, char **argv)
{   
    int x = 0;
    
    while(1)
    {       
        cout << "Podaj x."<< endl;
        cout << "x=";
        cin >> x;
        cout << "" << endl;
        
        if(x>=0 && x<=15)
        {   
            break;
        }
        
    }
    
    return 0;
}
