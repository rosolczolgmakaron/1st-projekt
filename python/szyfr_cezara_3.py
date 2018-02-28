#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):
    """Szyfrowanie tekstu za pomoca szyfru Cezara"""
    klucz = klucz % 26
    szyfrogram = ""
    # znaki_pl = ["Ą", "Ć", "Ę", "Ł", "Ń", "Ó", "Ś", "Ź", "Ż", "ą", "ć", "ę",
    #         "ł", "ń", "ó", "ś", "ź", "ż"]
    for i in tekst:
        ascii = ord(i) + klucz
        # print(ascii)
        if ord(i) == 32:  # szyfracja spacji
            ascii = 32
        if ord(i) == 46:  # szyfracja kropek
            ascii = 46
        if ascii > 90 and ascii < 97 or ascii > 122:
            ascii -= 26
        if i.isdigit() and ascii > 57:  # szyfracja cyfr
            ascii -= 10

        szyfrogram += chr(ascii)

    return szyfrogram


# troche duzo ifow, ale narazie nwm jak to przyspieszyc i uproscic. wazne ze dziala
def deszyfruj(szyfrogram, klucz):
    tekst = ""
    for i in szyfrogram:
        ascii = ord(i) - klucz
        # print(ascii)
        if ord(i) == 32:  # deszyfracja spacji
            ascii = 32
        if ord(i) == 46:  # deszyfracja kropek
            ascii = 46
        if ascii < 65 and ascii != 32 and ascii != 46:
            ascii += 26
        if ascii > 90 and ascii < 97 and ascii != 32 and ascii != 46:
            ascii += 26
        # print(i, ascii)
        if i != "." and ascii == 46:  # to niweluje buga sprawiajacego,
                                     # że 8 => "RS" gdyz linia 37 go powoduje
            ascii += 26
        # print(i, ascii)

        if i.isdigit():  # deszyfracja cyfr cyfr
            # print(ascii)
            ascii -= 26
            if ascii < 48:
                ascii += 10
            # print(ascii)
        tekst += chr(ascii)

    return tekst

# oblsłuzyć male i duże litery
# obsluzyc spacje
# sprawdzajka: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz Bartosz Gnatowski urodzony 02.11.2000 roku w Sandomierzu 0123456789


def main(args):
    tekst = input("Podaj tekst: ")
    klucz = int(input("Podaj klucz: "))

    while klucz > 6:
         klucz = int(input("Podaj klucz: "))

    szyfrogram = szyfruj(tekst, klucz)
    # szyfrogram = "VCBIU FHCDUD MHVW SURVWB"
    # klucz = 3
    print("Zaszyfrowane: ", szyfrogram)
    print("Deszyfrowane: ", deszyfruj(szyfrogram, klucz))

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
