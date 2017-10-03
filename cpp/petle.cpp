/*
 * pętle
 */
 
 
 #include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int i;
    
    for(i = 10; i <= 100; i++ )
    {
        if (i % 10 == 0)
        {
            cout << i << endl;
            ;
        }
        //cout << '*' << endl;
    }
    
    return 0;
}
