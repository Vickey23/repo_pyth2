class Czytelnik:
    id: int = 0

    def __init__(self, imie: str, nazwisko: str, nr_karty: int, mail: str):
        Czytelnik.id =+ 1

        self.id = Czytelnik.id
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_karty = nr_karty
        self.mail = mail
    
czyt1 = Czytelnik("Kuba", "Kot", "0000000001", "kuba@kot.pl")
czyt2 = Czytelnik("Tomasz", "Pies", "0000000002", "tom@pies.pl")
czyt3 = Czytelnik("Ania", "Lis", "0000000003", "anka@lisek.pl")
czyt4 = Czytelnik("Marta", "Szop", "0000000010", "szopi@szop.pl")

print(czyt4, czyt1, czyt3, czyt2)