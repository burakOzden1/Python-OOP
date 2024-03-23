# Kalitim, alt sinif turetme, alt siniflarla calisma


class Personel:

    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@gmail.com'


    def tam_isim(self): # regular method
        return f'{self.isim} {self.soyisim}'
    
    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)

#### METHOD RESOLUTION ORDER - KALITIM ZINCIRI
class Yazilimci(Personel):
    zam_orani = 1.1


yaz_1 = Yazilimci('Burak', 'Özden', 30000)
yaz_2 = Personel('Ahmet', 'Smith', 35000)
print(yaz_1.eposta)
print(yaz_2.eposta)

print(help(Yazilimci))

print(yaz_1.maas)
yaz_1.zam_uygula()
print(yaz_1.maas)

print(yaz_2.maas)
yaz_2.zam_uygula()
print(yaz_2.maas)

print(help(Yazilimci))

print(yaz_1.eposta)
print(yaz_1.prog_dili)