wiek = int(input("Podaj wiek: "))
kat = True if input("Czy posiadasz kat A2 (y/n)? ") \
    in ("y", "yes") else False
ile = int(input("Od ilu (ilość lat)? "))

if wiek >= 24 or kat == True and ile >=2:
    print("Możesz przystąpić do egzaminu!")
else:
    print("Nie możesz przystąpić do A")