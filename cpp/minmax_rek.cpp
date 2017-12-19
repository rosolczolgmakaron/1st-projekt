#include <iostream>

using namespace std;

void znajdzMinMax(int tab[],int i,int &maximum,int &minimum, int len )
{
if(i<len){
if (tab[i]<minimum)minimum=tab[i];
if (tab[i]>maximum)maximum=tab[i];
znajdzMinMax(tab,i+1,maximum,minimum,len);
}
}
void wypisz(int tab[],int i,int len )
{
if(i<len){
cout<<tab[i]<<' ';
wypisz(tab,i+1,len);
}
}
int NWD(int a, int b)
{
if(a!=b){
if (a>b) return NWD(b,a-b);
else return NWD(a,b-a);
}
return a;
}
int main()
{
int tab[]={4,3,5,6,7,1,21,45,9,56},minimum,maximum,a=24,b=16;
minimum=tab[0];
maximum=tab[0];
znajdzMinMax(tab,1,maximum,minimum,10);
wypisz(tab,0,10);
cout<<endl;
cout<<"Minimum:"<<minimum<<endl;
cout<<"Maximum:"<<maximum<<endl;
cout<<NWD(a,b)<<endl;
system("pause");
