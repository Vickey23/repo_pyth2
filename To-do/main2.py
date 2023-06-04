import json

class Zadania:
    def __init__(self):
        self.zadania = []
        self.zaladuj_zadania()

    def zaladuj_zadania(self):
        try:
            with open('Zadania.json', 'r') as f:
                self.zadania = json.load(f)
        except FileNotFoundError:
            print("Nie znaleziono pliku")
            pass

    def zapisz_do_pliku(self):
        with open('Zadania.json', 'w') as file:
            json.dump(self.zadania, file)

    def dodaj_zadanie(self):
        tytul = input("Tytuł zadania: ")
        opis = input("Opis zadania: ")
        data = input("Termin wykonania zadania: ")

        zadanie = {
            'id': len(self.zadania) + 1,
            'tytul': tytul,
            'opis': opis,
            'data': data
        }

        self.zadania.append(zadanie)
        self.zapisz_do_pliku()

        print("Twoje zadanie zostało dodane.")
        print("")

    def usun_zadanie(self):
        zadanie_id = int(input("Podaj ID zadania, które chcesz usuniąć: "))

        for zadanie in self.zadania:
            if zadanie['id'] == zadanie_id:
                self.zadania.remove(zadanie)
                self.zapisz_do_pliku()
                print("Zadanie usunięte.")
                print("")
                return

        print("Błedne ID.")
        print("")

    def zaktualizuj_zadania(self):
        zadanie_id = int(input("Podaj ID zadania, które chcesz zaktualizować: "))

        for zadanie in self.zadania:
            if zadanie['id'] == zadanie_id:
                tytul = input("Podaj nowy tytuł zadania: ")
                opis = input("Podaj nowy opis zadania: ")
                data = input("Podaj nowy termin wykonania zadania: ")

                zadanie['title'] = tytul
                zadanie['description'] = opis
                zadanie['due_date'] = data

                self.zapisz_do_pliku()
                print("Zadanie zaktualizowane.")
                print("")
                return

        print("Błedne ID.")
        print("")

    def pokaz_zadania(self):
        if len(self.zadania) == 0:
            print("Brak zapisanych zadań.")
            print("")
        else:
            for zadanie in self.zadania:
                print("ID: ", zadanie['id'])
                print("Tytuł: ", zadanie['title'])
                print("Termin wykonania: ", zadanie['due_date'])
                print("")

    def menu(self):
        while True:
            print("****menu zadań****")
            print("1 - Dodaj nowe zadanie")
            print("2 - Usuń zadanie")
            print("3 - Zaktualizuj zadanie")
            print("4 - Wyświetl zadania")
            print("5 - Zapisz zadania do pliku")
            print("6 - Wyjście")
            wybor = input("Wybierz opcję: ")

            if wybor == '1':
                self.dodaj_zadanie()
            elif wybor == '2':
                self.usun_zadanie()
            elif wybor == '3':
                self.zaktualizuj_zadania()
            elif wybor == '4':
                self.pokaz_zadania()
            elif wybor == '5':
                self.zapisz_do_pliku()
                print("Zadania zostały zapisane do pliku.")
            elif wybor == '6':
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie")

if __name__ == '__main__':
    task_manager = Zadania()
    task_manager.menu()
