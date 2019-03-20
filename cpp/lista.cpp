#include <iostream>
using namespace std;

struct wezel {
    int liczba;
    wezel *next;
};

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

