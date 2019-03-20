#include <iostream>

using namespace std;

int rozmiar = 3;
int dane[3];
int sp = 0;

void empty() {
    if (sp == 0) {
        cout << "Stos pusty" << endl;
    } else {
        cout << "Stos nie jest pusty" << endl;
    }
}

void pop() {
    if (sp-1 < 0) {
        cout << "Stos pusty!";
    } else {
        cout << "POP: " << dane[sp-1] << endl;
        sp--;
    }
}

void push() {
    if (sp > rozmiar - 1) {
        cout << "Stos pełny!" << endl;
    } else {
        cout << "Podaj wartość: ";
        cin >> dane[sp];
        sp++;
    }
}

int main(int argc, char **argv)
{
    push();
    cout << sp << endl;
    push();
    cout << sp << endl;
    push();
    cout << sp << endl;
    push();
    
    pop();
    cout << sp << endl;
    pop();
    cout << sp << endl;
    pop();
    cout << sp << endl;
    pop();
    return 0;
}
