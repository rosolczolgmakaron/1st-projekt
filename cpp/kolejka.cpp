#include <iostream>
using namespace std;

int rozmiar = 3;
int dane[3];
int head = 0;
int tail =0;
int ile = 0;

void pop() {
    if (ile == 0) {
        cout << "Kolejka pusta!";
        head = 0;
    } else {
        cout << dane[head];
        tail=head;
        head++;
        ile--;
    }
}

void push() {
    if (ile >= rozmiar) {
        cout << "Kolejka pełna!" << endl;
    } else {
        cout << "Podaj wartośc: ";
        cin >> dane[tail];
        tail++;
        ile++;
    }
}

int main(int argc, char **argv)
{
    push();
    push();
    push();


	return 0;
}

