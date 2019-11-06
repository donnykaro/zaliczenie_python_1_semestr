def pobranie_liczby_przypadkow():
    while True:
        try:
            liczba_przypadkow = int(input())
        except ValueError:
            print("Liczba przypadkow musi być typu int")
        else:
            if liczba_przypadkow < 0:
                print("Liczba przypadkow nie moze byc mniejsza od 0")
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


jest_tribbionacci = {}
bledne_dane = False
for i in range(0, pobranie_liczby_przypadkow()):
    liczba_uzytkownika = pobranie_liczby()
    if liczba_uzytkownika <= 2:
        bledne_dane = True
    else:
        jest_tribbionacci[liczba_uzytkownika] = False

# t1=0
# t2=1
# t3=2
# t4=3
# t5=6
# t6=11
# t7=20

wynik = 0
for przypadek in jest_tribbionacci:
    wynik = 0
    T_minus_3 = 0
    T_minus_2 = 1
    T_minus_1 = 2
    for i in range(2, przypadek):
        wynik = T_minus_1 + T_minus_2 + T_minus_3
        if wynik == przypadek:
            jest_tribbionacci[przypadek] = True
            break
        else:
            jest_tribbionacci[przypadek] = False
        T_minus_3 = T_minus_2
        T_minus_2 = T_minus_1
        T_minus_1 = wynik


for przypadek in jest_tribbionacci:
    if jest_tribbionacci[przypadek] == True:
        print(str(przypadek) + "\tTAK")
    else:
        print(str(przypadek) + "\tNIE")

if bledne_dane == True:
    print("Blad")