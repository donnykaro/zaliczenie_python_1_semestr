import sys

jest_tribbonacci = {}
bledne_dane = False

def pobranie_liczby_przypadkow():
    while True:
        try:
            liczba_przypadkow = int(input())
        except ValueError:
            print("Liczba przypadkow musi być typu int")
        else:
            if liczba_przypadkow < 0:
                print("Blad")
                sys.exit(0)
            else:
                return liczba_przypadkow


def pobranie_liczby():
    while True:
        try:
            liczba_temp = int(input())
        except ValueError:
            print("Podana Liczba musi być typu int")
        else:
            return liczba_temp


for i in range(0, pobranie_liczby_przypadkow()):
    liczba_uzytkownika = pobranie_liczby()
    if liczba_uzytkownika <= 2:
        bledne_dane = True
    else:
        jest_tribbonacci[liczba_uzytkownika] = False

T_minus_3 = 0
T_minus_2 = 1
T_minus_1 = 2
for przypadek in sorted(jest_tribbonacci):
    while True:
        wynik = T_minus_1 + T_minus_2 + T_minus_3

        if wynik == przypadek:
            jest_tribbonacci[przypadek] = True
            break
        else:
            jest_tribbonacci[przypadek] = False

        if wynik > przypadek:
            break

        T_minus_3 = T_minus_2
        T_minus_2 = T_minus_1
        T_minus_1 = wynik


for przypadek in jest_tribbonacci:
    if jest_tribbonacci[przypadek]:
        print(str(przypadek) + "\tTAK")
    else:
        print(str(przypadek) + "\tNIE")


if bledne_dane:
    print("Blad")
