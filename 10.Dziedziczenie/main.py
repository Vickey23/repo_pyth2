from abc import ABC, abstractmethod
import math

class Kształt(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def pole(self):
        pass

    @abstractmethod
    def obwod(self):
        pass


class Kwadrat(Kształt):

    def __init__(self, dlugosc_boku: int):
        self.__dlugosc_boku = dlugosc_boku

    def pole(self):
        return self.__dlugosc_boku * self.__dlugosc_boku
    
    def obwod(self):
        return self.__dlugosc_boku * 4
    

class Kolo(Kształt):

    def __init__(self, srednica: int):
        super().__init__()
        self.__srednica = srednica

    def obwod(self):
        return math.pi * self.__srednica**2
    
    def pole(self):
        return 2 * math.pi * self.__srednica
    

class Prostokat(Kształt):

    def __init__(self, dlugosc_boku_a: int, dlugosc_boku_b):
        self.__dlugosc_boku_a = dlugosc_boku_a
        self.__dlugosc_boku_b = dlugosc_boku_b

    def pole(self):
        return self.__dlugosc_boku_a * self.__dlugosc_boku_b
    
    def obwod(self):
        return (self.__dlugosc_boku_a + self.__dlugosc_boku_b) * 2
        

while True:
    print("Jaką figurę wybierasz?")
    print("1 - kwadrat")
    print("2 - koło")
    print("3 - prostokąt")
    print("4 - koniec :)")

    wybor = int(input("Twój wybór: "))

    if wybor == 1:
        a = int(input("Długość boku: "))
        kwadrat = Kwadrat(a)
        print("Pole jest równe: ", kwadrat.pole())
        print("Obwód jest równy: ", kwadrat.obwod())
    
    elif wybor == 2:
        a = int(input("Długość średnicy: "))
        kolo = Kolo(a)
        print("Pole jest równe: ", kolo.pole())
        print("Obwód jest równy: ", kolo.obwod())

    elif wybor == 3:
        a = int(input("Długość boku a: "))
        b = int(input("Długość boku b: "))
        prostokat = Prostokat(a, b)
        print("Pole jest równe: ", prostokat.pole())
        print("Obwód jest równy: ", prostokat.obwod())

    elif wybor == 4:
        print("Papa :)")
        break

    else:
        print("****Błędny numer!****")