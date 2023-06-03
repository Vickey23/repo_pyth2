def dodawanie(a, b):
    wynik = a + b
    print(wynik)

def odejmowanie(a, b):
    wynik = a - b
    print(wynik)

def mnozenie(a, b):
    wynik = a * b
    print(wynik)

def dzielenie(a, b):
    if b == 0:
        print("nie dziel przez 0")
        return
    wynik = a / b
    print(wynik)

while True:
    print("1 - dodawanie")
    print("2 - odejmowanie")
    print("3 - mnożenie")
    print("4 - dzielenie")
    print("9 - koniec")

    wybor = int(input("Wybierz opcje: "))

    if wybor == 1:
        a = int(input("pierwsza liczba: "))
        b = int(input("druga liczba: "))
        dodawanie(a, b)
    elif wybor == 2:
        a = int(input("pierwsza liczba: "))
        b = int(input("druga liczba: "))
        odejmowanie(a, b)
    elif wybor == 3:
        a = int(input("pierwsza liczba: "))
        b = int(input("druga liczba: "))
        mnozenie(a, b)
    elif wybor == 4:
        a = int(input("pierwsza liczba: "))
        b = int(input("druga liczba: "))
        dzielenie(a, b)
    elif wybor == 9:
        print("Dalej liczysz sam")
        break