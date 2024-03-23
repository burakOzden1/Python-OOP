# Kalitim, alt sinif turetme, alt siniflarla calisma


class Personel:

    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@gmail.com'
        print(f'Yeni Personel Tanimlandi : {isim} {soyisim}')


    def tam_isim(self): # regular method
        return f'{self.isim} {self.soyisim}'
    
    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)

#### METHOD RESOLUTION ORDER - KALITIM ZINCIRI
class Yazilimci(Personel):
    # yazilimci nesnelerinin zam oranlarini farkli yaptik.
    zam_orani = 1.1

    def __init__(self, isim, soyisim, maas, prog_dili):
        # super ifadesi Personel sinifi icerisinde tanimlanan isim, soyisim, maas ve eposta gibi degisken tanimlamalarini getirir. Bunun yerine "Personel.__init__(self, isim, soyisim, maas)" ifadesini yazabiliriz, aynı anlama gelir.
        super().__init__(isim, soyisim, maas)
        self.prog_dili = prog_dili
        print(f'Yeni Personel Yazilimci Kategorisine Tasindi : {self.isim} {self.soyisim}')



yaz_1 = Yazilimci('Burak', 'Özden', 30000, "python")
yaz_2 = Personel('Ahmet', 'Smith', 35000)
# print(yaz_1.eposta)
# print(yaz_2.eposta)

# print(help(Yazilimci))

print(yaz_1.maas)
yaz_1.zam_uygula()
print(yaz_1.maas)

print(yaz_2.maas)
yaz_2.zam_uygula()
print(yaz_2.maas)

# print(help(Yazilimci))

print(yaz_1.eposta)
print(yaz_1.prog_dili)