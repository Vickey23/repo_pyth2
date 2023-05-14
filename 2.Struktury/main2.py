slowo = input("podaj słowo: ")

odwrocone = slowo[::-1]

if odwrocone == slowo:
    print("Oto twój palindrom!")
else:
    print("To nie jest palindrom..")