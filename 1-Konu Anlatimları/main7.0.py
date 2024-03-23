# Encapsulation / Kapsülleme


class Personel:
    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.__zam_orani = 1.05

    def getZamOrani(self):
        return self.__zam_orani
    
    def setZamOrani(self, oran):
        self.__zam_orani = oran

    def zam_uygula(self):
        self.maas = int(self.maas * self.__zam_orani)


per_1 = Personel('Burak', 'Özden', 30000)

# print(per_1.isim)
# print(per_1.maas)
# print(per_1.zam_orani)
# per_1.zam_orani = 1.2
# per_1.zam_uygula()
# print('Yeni maas miktari : ', per_1.maas)
# zam orani degiskeninin disaridan erisilerek degistirilmesini istemiyorum, bu yüzden basina __ ifadesini koydum.

print(per_1.__dict__)
print(per_1.__zam_orani) # hata aliriz cunku kapsulleyerek bu degiskene erisilmesini engelledik.

# zam orani ifadesini goruntulemek istiyoruz, bunun icin get fonksiyonundan faydalaniriz. getZamOrani adinda bir ifade kullarak bu islemi gerceklestirebiliriz.

print(per_1.getZamOrani())


# set fonksiyonunu kullanarak da kapsulledigimiz fonksiyonu degistirebiliriz, tamam kapsulledik ama bir arka kapi acmak istiyoruz diyelim. (mantikli olan yapmamak)

print(per_1.getZamOrani())
per_1.setZamOrani(oran=1.2)
print(per_1.getZamOrani())

# ! sinifimiz icindeki degisleri kapsulleyebildigimiz gibi methodlarin basina __ ifadesini getirerek methodlar uzerinde de kapsulleme islemini gerceklestirebiliriz.