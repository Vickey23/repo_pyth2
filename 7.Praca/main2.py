from os import path
import random

dir_path = path.dirname(__file__)
plik1 = "imiona.txt"
plik2 = "nazwiska.txt"
nowy_plik = "wynik.txt"
dane_plik1 = path.join(dir_path, plik1)
dane_plik2 = path.join(dir_path, plik2)
dane_nowy = path.join(dir_path, nowy_plik)

if not path.exists(dane_plik1) or not path.exists(dane_plik2):
    exit()


with open(dane_plik1, 'r', encoding="utf-8") as f:
    imiona = [line.strip() for line in f.readlines()]


with open(dane_plik2, 'r', encoding="utf-8") as f:
    nazwiska = [line.strip() for line in f.readlines()]


maks_ilosc = len(imiona) * len(nazwiska)


try:
    ilosc_uzytk = int(input("Wpisz ile chcesz kombinacji: "))
    if ilosc_uzytk == 0 or ilosc_uzytk > maks_ilosc:
        print(f"Wpisz liczbę między 1 a {maks_ilosc}!")
        exit()
except:
    print("Błąd wpisywanej liczby")
    exit()


kombinacje = []
        

for imie in imiona:
    if(len(kombinacje) == ilosc_uzytk): break
    for nazwisko in nazwiska:
        kombinacje.append(imie + " " + nazwisko)
        if(len(kombinacje) == ilosc_uzytk): break

with open(dane_nowy, "w", encoding="utf-8") as f:
    for kombinacja in kombinacje:
        f.write(kombinacja + "\n")
    f.close()


print("Twoje kombinacje: ")
for i in range (len(kombinacje)):
    print(f"{i+1}. {kombinacje[i]}")