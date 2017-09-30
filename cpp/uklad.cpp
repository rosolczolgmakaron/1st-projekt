 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int x, y;
    x = y = 0;
    
    cout << "Podaj współrzędną x:";
    cin >> x;
    cout << "Podaj współrzędną y:";
    cin >> y;
    
    if (x>0 && y>0)
    {
    cout << "Punkt o współrzędnych  (" << x << "," << y << ") znajduje się w I ćwiartce." << endl;    
    }
    
    if (x<0 && y>0)
    {
    cout <<"Punkt o współrzędnych  (" << x << "," << y << ") znajduje się w II ćwiartce." << endl;    
    }
    
    if (x<0 && y<0)
    {
    cout <<"Punkt o współrzędnych  (" << x << "," << y << ") znajduje się w III ćwiartce." << endl;    
    }
    
    if (x>0 && y<0)
    {
    cout << "Punkt o współrzędnych  (" << x << "," << y << ") znajduje się w IV ćwiartce." << endl;
    }
    
    
    {
    cout << "Punkt o współrzędnych  (" << x << "," << y << ") znajduje się na osi Ox." << endl;
    }
    return 0;
}
