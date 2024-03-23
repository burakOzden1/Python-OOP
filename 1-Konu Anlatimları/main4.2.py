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


class Yazilimci(Personel):
    zam_orani = 1.1

    def __init__(self, isim, soyisim, maas, prog_dili):
        super().__init__(isim, soyisim, maas)
        self.prog_dili = prog_dili


class Mudur(Personel):
    def __init__(self, isim, soyisim, maas, personeller=None):
        super().__init__(isim, soyisim, maas)
        if personeller is None:
            self.personeller = []
        else:
            self.personeller = personeller

    def personel_ekle(self, per):
        if per not in self.personeller:
            self.personeller.append(per)

    def personel_cikar(self, per):
        if per in self.personeller:
            self.personeller.remove(per)

    def personelleri_listele(self):
        for e, per in enumerate(self.personeller):
            e += 1
            print(e, per.tam_isim())


yaz_1 = Yazilimci('Burak', 'Özden', 30000, "python")
yaz_2 = Yazilimci('Ahmet', 'Smith', 35000, "java")
yaz_3 = Yazilimci('Ayşe', 'Akyol', 35000, "html")

mdr_1 = Mudur('Ali', 'Kurt', 50000, [yaz_1, yaz_2])
mdr_2 = Mudur('İhsan', 'Şen', 45000)

print(mdr_1.tam_isim())
print("************")
mdr_1.personelleri_listele()
print("************")
mdr_1.personel_ekle(yaz_3)
print("************")
mdr_1.personelleri_listele()
mdr_1.personel_cikar(yaz_2)
print("************")
mdr_1.personelleri_listele()
mdr_2.personelleri_listele()
mdr_2.personel_ekle(yaz_1)
mdr_2.personelleri_listele()


################ !!!!!!!!!!!!!!!!!! #################

# isinstance()
print("yaz_1 yazilimci sinifindan mi uretilmis : ", isinstance(yaz_1, Yazilimci))
print("yaz_1 personel sinifindan mi uretilmis : ", isinstance(yaz_1, Personel))
print("yaz_1 mudur sinifindan mi uretilmis : ", isinstance(yaz_1, Mudur))

# issubclass()
print("yazilimci sinifi personel sinifindan mi turetildi : ", issubclass(Yazilimci, Personel))
print("mudur sinifi personel sinifindan mi turetildi : ", issubclass(Mudur, Personel))
print("mudur sinifi yazilimci sinifindan mi turetildi : ", issubclass(Mudur, Yazilimci))