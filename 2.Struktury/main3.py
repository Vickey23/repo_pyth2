lista = ["burak","cukinia", "pomidor", "cytryna", "ananas", "papryka", "dynia"]

literka = input("Na jaką literkę chcesz słowa? ")

for i in lista:
    if i[0:1] == literka:
        print(i, end=" ")