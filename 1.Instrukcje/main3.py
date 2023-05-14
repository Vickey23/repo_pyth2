from random import randint

graj = True

while graj == True:
    ilosc = 1
    losowana = randint(0, 100)
    los = int(input("Podaj liczbę od 0 do 100: "))
    while los != losowana:
        if los < losowana:
            print("Za mała próbuj raz jeszcze!")
        elif los > losowana:
            print("Za duża próbuj raz jeszcze!")
        los = int(input("nowa liczba: "))
        ilosc += 1
    print(f"Brawo zgadłeś po {ilosc} razach!")
    if input("Grasz jeszcze? <t/n>?") != 't':
        graj = False
