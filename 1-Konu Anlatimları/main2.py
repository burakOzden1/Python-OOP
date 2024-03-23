


class Personel:

    personel_sayisi = 0
    zam_orani = 1.05
    yetkili_mi = False

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@gmail.com'
        Personel.personel_sayisi += 1

    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'
    
    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)
    
print("Personellerimi oluşturmadan önce : ", Personel.personel_sayisi)

per_1 = Personel('Burak', 'Özden', 30000)
per_2 = Personel('Ahmet', 'Smith', 35000)

print(per_1.maas)
per_1.zam_uygula()
print(per_1.maas)

print(Personel.zam_orani)
print(per_1.zam_orani)
print(per_2.zam_orani)


from pprint import pprint

pprint(per_1.__dict__) # burada per_1, sinif içerisindeki zam oranini kullaniyor ve bunu per_1 bilgileri içine yazdırmaya gerek duymuyor
print('_____________________________________________________')
pprint(Personel.__dict__)


Personel.zam_orani = 1.1 # burada ise per_1 için farkli bir zam orani belirledik
per_1.zam_orani = 1.15

pprint(per_1.__dict__) # burada ise per_1'in kendisine özel bir zam orani olduğu için bu orani per_1 bilgileri içerisinde görebildik
print(Personel.zam_orani)
print(per_1.zam_orani)
print(per_2.zam_orani)

print("Personellerimi oluşturduktan sonra : ", Personel.personel_sayisi)


per_1.yetkili_mi = True

pprint(per_1.__dict__)
print(Personel.yetkili_mi)