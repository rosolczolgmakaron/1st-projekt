/*
 * petla 
 */
 
 #include <iostream>
 #include <cmath>

using namespace std;

int main(int argc, char **argv)
{
    char zn='t';

    while(zn == 't' || zn == 'T' || zn == 'n' || zn == 'N' ) {
        cout<<"Podaj znak."<<endl;
        cin>>zn;

        //if(zn=='t' || zn=='T' || zn=='n' || zn=='N')
            //{
                //cout<<"Podany znak to "<< zn<< endl;
                //cout<< ""<< endl;
            //}
        //else
            //break;

    };
    return 0;
}
