import sys

jest_tribbonacci = {}
exception_counter = 0

def pobranie_liczby_przypadkow():
    while True:
        try:
            liczba_przypadkow = int(input())
        except ValueError:
            print('BLAD')
            sys.exit(0)
        else:
            if liczba_przypadkow <= 0:
                print('BLAD')
                sys.exit(0)
            else:
                return liczba_przypadkow


def pobranie_liczby():
    global exception_counter
    input_uzytkownika = input()
    try:
        liczba_temp = int(input_uzytkownika)
    except ValueError:
        jest_tribbonacci[input_uzytkownika+str(exception_counter)] = None
        exception_counter += 1
    else:
        if type(liczba_temp) == int:
            if liczba_temp <= 2:
                jest_tribbonacci[input_uzytkownika+str(exception_counter)] = None
                exception_counter += 1
            else:
                return liczba_temp


T_minus_3 = 0
T_minus_2 = 1
T_minus_1 = 2
for i in range(0, pobranie_liczby_przypadkow()):
    przypadek = pobranie_liczby()
    if type(przypadek) == int:
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
    if jest_tribbonacci[przypadek] is not None:
        if jest_tribbonacci[przypadek]:
            print(str(przypadek) + "\tTAK")
        else:
            print(str(przypadek) + "\tNIE")
    else:
        print('BLAD')
