


class Personel:
    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@gmail.com'

    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'
    

per_1 = Personel(isim = 'Burak', soyisim='Özden', maas=30000)
per_2 = Personel('Ahmet', 'Smith', 35000)

print(per_1.isim)
print(per_1.soyisim)
print(per_1.maas)
print(per_1.eposta)


print(per_1.tam_isim())
print(per_2.tam_isim())

print(Personel.tam_isim(per_1))
print(Personel.tam_isim(per_2))