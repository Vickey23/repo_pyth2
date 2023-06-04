import string
from os import path
dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

lista = []
liczenie = 0
staty = {}

with open(data_path, 'r', encoding="utf-8") as f:
    for i in range(3):
        linie = f.readline().strip()
        slowa = linie.split()
        lista.extend(slowa)
        for slowo in slowa:
            while len(slowo) > 0 and slowo[-1] in string.punctuation:
                slowo = slowo[:-1]
            if slowo:
                liczenie += 1
                ostatnia = slowo[-1]
                if ostatnia not in staty:
                    staty[ostatnia] = 1
                else:
                    staty[ostatnia] += 1

print (f"Ilość słów w linijce: {i+1}: {len(slowa)}")
print ("Końcowe literki słów: ")
for litera, count in staty.items():
    print(f"{litera}: {count} raz/y")

