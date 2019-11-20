import sys

jest_tribbonacci = []


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
    input_uzytkownika = input()
    try:
        liczba_temp = int(input_uzytkownika)
    except ValueError:
        jest_tribbonacci.append([input_uzytkownika, 'BLAD'])
    else:
        if type(liczba_temp) == int:
            if liczba_temp <= 2:
                jest_tribbonacci.append([input_uzytkownika, 'BLAD'])
            else:
                return liczba_temp


for i in range(0, pobranie_liczby_przypadkow()):

    T_minus_3, T_minus_2, T_minus_1 = 0, 1, 2

    przypadek = pobranie_liczby()
    if type(przypadek) == int:
        while True:
            wynik = T_minus_1 + T_minus_2 + T_minus_3

            if wynik == przypadek:
                jest_tribbonacci.append([przypadek, 'TAK'])
                break

            if wynik > przypadek:
                jest_tribbonacci.append([przypadek, 'NIE'])
                break

            T_minus_3, T_minus_2, T_minus_1 = T_minus_2, T_minus_1, wynik

for i in range(0, len(jest_tribbonacci)):
    if jest_tribbonacci[i][1] == 'BLAD':
        print(jest_tribbonacci[i][1])
    else:
        print(f"{jest_tribbonacci[i][0]}\t{jest_tribbonacci[i][1]}")
