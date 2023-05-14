krotka = (10,-3,4,9,12,-6,0)

print(f"Twoje liczby: {krotka}")

min = krotka[0]
max = krotka[0]

for i in krotka:
    if min > i:
        min = i
    if max < i:
        max = i

print(f"Największa: {max}, najmniejsza: {min}")