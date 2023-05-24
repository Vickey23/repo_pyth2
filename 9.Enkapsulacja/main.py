class Czytelnik:
    id: int = 0

    def __init__(self, imie: str, nazwisko: str, nr_karty: int, mail: str):
        Czytelnik.id =+ 1

        self.__id = Czytelnik.id
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__nr_karty = nr_karty
        self.__mail = mail

    def pobierz_id(self):
        return self.__id
    def pobierz_imie(self):
        return self.__imie
    def pob_naz(self):
        return self.__nazwisko
    def pob_nr_karty(self):
        return self.__nr_karty
    def pob_mail(self):
        return self.__mail
    
czyt1 = Czytelnik("Kuba", "Kot", "0000000001", "kuba@kot.pl")
czyt2 = Czytelnik("Tomasz", "Pies", "0000000002", "tom@pies.pl")
czyt3 = Czytelnik("Ania", "Lis", "0000000003", "anka@lisek.pl")
czyt4 = Czytelnik("Marta", "Szop", "0000000010", "szopi@szop.pl")

print(czyt3.pob_nr_karty())