/*
 * pętle
 */
 
 
 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    for(int i = 1; i <= 100; i++ )
    {
        if (i%10 == 0)
        {
            cout << i << endl;
            ;
        }
        cout << '*' << endl;
    }
    
    return 0;
}
