#include <iostream>

using namespace std;

struct punkt
{
    int x;
    int y;
};

struct wektor
{
    punkt pp;
    punkt pk;
};

wektor getWektor()
{
    wektor w1;
    cout << "Podaj x, y punktu początkowego:\n";
    cin >> w1.pp.x;
    cin >> w1.pp.y;
    cout << "Podaj x, y punktu końcowego:\n";
    cin >> w1.pk.x;
    cin >> w1.pk.y;
    
    return w1;
}

punkt wylicz_srodek(wektor w)
{
    punkt ps;
    ps.x = (w.pk.x + w.pp.x)/2;
    ps.y = (w.pk.y + w.pp.y)/2;
    return ps;
}

int main(int argc, char **argv)
{
    wektor w;
    punkt ps;
    w = getWektor();
    ps = wylicz_srodek(w);
    cout << "Wektor: " << "(" << w.pp.x << ", " << w.pk.y << ")" << endl;
    cout << "Środek: " << ps.x << ", " << ps.y << endl;
	return 0;
}

