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
    
    def __add__(self, other):
        return self.maas + other.maas
    
    def __len__(self):
        return len(self.tam_isim())
    

per_1 = Personel('Burak', 'Özden', 30000)
per_2 = Personel('Ahmet', 'Smith', 35000)

print(1 + 2) # print(int.__add__(1, 2))
print("a", "b") # print(str.__add__("a", "b"))


### Iki personelimizin toplam maasini almak istiyo olalim, sinifimiz icinde __add__ fonksiyonumuzu yazdik.
print(per_1 + per_2) # print(per_1.__add__(per_2))

print(len("araba")) # print('araba'.__len__())


### personelimizin tam isminin uzunlugunu ogrenmek icin sinifimiz icerisinde bir __len__ methodu tanimladik.
print(len(per_1))



### bu konu hakkinda gercek yasamdan bazi orneklere bakalim

from datetime import datetime  # kutuphanesi icerisindeki bazi yapilarda yukarida ogrendigimiz pek cok konu kullanilmistir.
