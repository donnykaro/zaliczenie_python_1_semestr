liczba_przypadkow = int(input())
jest_tribbionacci = {}
bledne_dane = False
for i in range(0, liczba_przypadkow):
    liczba_uzytkownika = int(input())
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