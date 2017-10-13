/*
 * petla switch
 */
 
 #include <iostream>
 #include <cmath>

using namespace std;

int main(int argc, char **argv)
{
    int m=0;

    while(m > 12 || m < 1){
        cout<<"Podaj miesiąc (1-12)."<<endl;
        cin>>m;
        cout<<""<<endl;
    };
    
    switch(m)
    {
        case 1:
            cout<<"Styczeń";
        break;
        
        case 2:
            cout<<"Luty";
        break;
        
        case 3:
            cout<<"Marzec";
        break;
        
        case 4:
            cout<<"Kwiecień";
        break;
        
        case 5:
            cout<<"Maj";
        break;
    }

    return 0;
}
