# Ozel metotlar, DUNDER Methods, __str__, __repr__, __add__ gibi


class Personel:

    """
        Bu sinif tutoriallar kapsaminda hazirlandi.
        Bu sinifi kullanarak personeller olusturabilirsiniz.
    """

    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@gmail.com'

    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'
    
    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)

    # Bu ifade gelistiriciler icin bir bilgi saglar.
    def __repr__(self):
        return f"Personel('{self.isim}', '{self.soyisim}', {self.maas})"
    
    # Bu ifade is son kullanicilar icin daha okunabilir bir ifade saglar.
    def __str__(self):
        return f"{self.tam_isim()} - {self.eposta}"
    

per_1 = Personel('Burak', 'Özden', 30000)
per_2 = Personel('Ahmet', 'Smith', 35000)

print(per_1) # varsayilan olarak str methodu calisir.
print(str(per_1)) # print(per_1.__str__())
print(repr(per_1)) # print(per_1.__repr__())
print(help(per_1))