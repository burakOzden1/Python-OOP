


class Personel:

    personel_sayisi = 0
    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@gmail.com'
        Personel.personel_sayisi += 1

    def tam_isim(self): # regular method
        return f'{self.isim} {self.soyisim}'
    
    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)

    @classmethod
    def zam_oranini_belirle(cls, oran): # class method
        eski_oran = cls.zam_orani
        cls.zam_orani = oran
        print(f'Eski zam orani ({eski_oran}) guncellendi. Yeni oran: {cls.zam_orani}')

    @classmethod
    def from_string(cls, per_str):
        isim, soyisim, maas = per_str.split("-")
        return cls(isim, soyisim, int(maas)) # gelen yeni nesneyi olusturduk ve dondurduk.
    

    @staticmethod
    def mesai_gunu(gun): # static method
        if gun.weekday() == 5 or gun.weekday() == 6:
            return 'Hafta Sonu'
        else:
            return 'Hafta İçi'
        
    
print("Personel sayisi : ", Personel.personel_sayisi)

per_1 = Personel('Burak', 'Özden', 30000)
per_2 = Personel('Ahmet', 'Smith', 35000)


print(Personel.zam_orani)

Personel.zam_oranini_belirle(1.3)
# Personel.zam_orani = 1.3 # ustteki ifade ile ayni isi yapar

print(Personel.zam_orani)
print(per_1.zam_orani)
print(per_2.zam_orani)

per_str_1 = 'Ali-Atay-5000'
per_str_2 = 'Raziye-Kuşçu-8000'
per_str_3 = 'Fuat-Çalık-10000'

yeni_per_1 = Personel.from_string(per_str_1)

print(yeni_per_1.isim)
print(yeni_per_1.soyisim)
print(yeni_per_1.maas)


print(yeni_per_1.zam_orani)
yeni_per_1.zam_uygula()
print(yeni_per_1.maas)

############### static method #################

import datetime
tarih = datetime.date(2021, 6, 19)
print(tarih.day)
print(Personel.mesai_gunu(tarih))