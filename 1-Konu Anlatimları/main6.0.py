# Property Decorators, getters, setters


class Personel:

    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas

    @property
    def eposta(self):
        return f'{self.isim.lower()}.{self.soyisim.lower()}@gmail.com'

    @property
    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'
    
    @tam_isim.setter
    def tam_isim(self, ad):
        isim, soyisim = ad.split(' ')
        self.isim = isim
        self.soyisim = soyisim

    @tam_isim.deleter
    def tam_isim(self):
        print('DEGISKENLER SILINDI!!!')
        self.isim = None
        self.soyisim = None

per_1 = Personel('Burak', 'Özden', 30000)

# diyelim ki yukaridaki isim ifadesini yanlis girdik ve duzeltmek istiyoruz, bunun icin sinifimiz icerisinde bulunan eposta alanini sildik ve bunu bir method olarak yazdik. Daha sonra ismimizi degistirip yazdirmak istedigimizde per_1.eposta() seklinde bir ifade kullanmamiz gerekir ama biz direkt bir degisken olarak cagirmak istiyoruz, yani sondaki parantezleri kullanmadan cagirmak istiyoruz. Bunun icinde sinif icerisindeki eposta methodumuzun üzerine @property bezeyicisini eklemek zorundayiz.
per_1.isim = "Berk"
print(per_1.isim)
print(per_1.eposta)
print(per_1.tam_isim())

# ayni kullanimi tam_isim fonksiyonumuzun uzerinde de yapabiliriz.


# gelelim baska bir soruna: diyelim ki kullanici per_1.isim alanina tek isim girmek yerine ismini ve soyisimini girdi. Sinifimizi bu ihtimale gore duzenleyelim. Tam isim methoduyla ayni isimde yeni bir method tanimladik ve gelen parametreyi ad parametresi ile aldik, split ile bosluktan ayirdik.

per_1.tam_isim = 'Ahmet Çarpık'
print(per_1.isim)

# ifadelerimizi silmek icin ise deleter adli bir decorator kullaniriz.
del per_1.tam_isim
print(per_1.isim)