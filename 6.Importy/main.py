import modul

def kalkulator() -> None:
    """Funkcja wyboru opcji liczenia"""
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
            modul.dodawanie(a, b)
        elif wybor == 2:
            a = int(input("pierwsza liczba: "))
            b = int(input("druga liczba: "))
            modul.odejmowanie(a, b)
        elif wybor == 3:
            a = int(input("pierwsza liczba: "))
            b = int(input("druga liczba: "))
            modul.mnozenie(a, b)
        elif wybor == 4:
            a = int(input("pierwsza liczba: "))
            b = int(input("druga liczba: "))
            modul.dzielenie(a, b)
        elif wybor == 9:
            print("Dalej liczysz sam")
            break

kalkulator()