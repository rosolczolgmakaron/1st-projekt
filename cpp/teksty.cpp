/*
* tabele.cpp
*/

 #include <iostream>
 #include <cmath>

using namespace std;

int main(int argc, char **argv)
{
    int i;
    for (i=65; i<=90; i++)
    {
        cout<< i << " " << char(i) << endl;
    }
    
    for (i=97; i<=122; i++)
    {
        cout<< i << " " << char(i) << endl;
    }

    char osoba[25];
    cout<< "Jak się nazywasz?"<<endl;
    //cin>> osoba;
    cin.getline(osoba, 25);
    cout<< "Hej, "<< osoba << "!" << endl;




    //~char znak= 'a';
    //~char znak2= 'b';
    //~cout<< znak<<" "<< int(znak)<< endl;
    //~cout<< znak2<<" "<< int(znak2)<< endl;

    return 0;
}
