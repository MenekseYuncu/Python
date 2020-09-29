"""
class halka:
    halka_sayisi = 5

    def halka_at(self):
        print("Bir adet halka atıldı")
        self.halka_sayisi -= 1

    def kac_halka_kaldı(self):
        if(self.halka_sayisi <= 0):
            print("Hiç halka kalmadı ")
        else:
            print(str(self.halka_sayisi) + "Kadar halkanız kaldı")


halka_1 = halka()
halka_2 = halka()


halka_1.halka_at()
halka_1.halka_at()
halka_1.kac_halka_kaldı()



class dusman:

    def __init__(self, isim="Dusman", kalan_can=500, saldiri_gucu=70, mermi_sayisi=6):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def print(self):
        print("Ready ----------")
        print("İsim:", self.isim, "Kalan Can:", self.kalan_can, "Saldırı Gucu:",
              self.saldiri_gucu, "Mermi Sayısı:", self.mermi_sayisi)


dusman1 = dusman("Butterfly", 60, 15, 9)
dusman2 = dusman("Cat", 90, 100, 7)
dusman3 = dusman()

dusman1.print()
print("BUTTERFLY*********")
dusman2.print()
print("CAT***********")
dusman3.print()
print("DUSMAN*****")
"""


import random


class Dusman:
    def __init__(self, isim, kalan_can, saldiri_gucu, mermi_sayisi):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim + "SALDIRIYOR")
        harcanan_mermi = random.randrange(0, 10)
        print(str(harcanan_mermi)+"KADAR KALDI")
        self.mermi_sayisi -= harcanan_mermi

        return (harcanan_mermi, self.saldiri_gucu)

    def saldiriyaugra(self, harcanan_mermi, saldiri_gucu):
        print("VURULDUM....")
        self.kalan_can -= (harcanan_mermi * saldiri_gucu)

    def mermi_bitti_mi(self):
        if (self.mermi_sayisi <= 0):
            print(self.isim + "TESLİM OLUYORUM")
            return True
        return False

    def hayatta_mi(self):
        if (self.kalan_can <= 0):
            print("ÖLDÜN...")

    def print(self):
        print("BAŞLIYOR")
        print("isim:", self.isim, "Kalan Can:", self.kalan_can, "Saldırı Gucu:",
              self.saldiri_gucu, "Mermi Sayısı:", self.mermi_sayisi)


dusmanlar = []

i = 0
while (i < 10):
    rastgelecan = random.randrange(100, 200)
    rastgelesaldirigucu = random.randrange(10, 20)
    rastgelemermi = random.randrange(10, 15)
    yenidusman = Dusman("Dusman" + str(i+2), rastgelecan,
                        rastgelesaldirigucu, rastgelemermi)

    dusmanlar.append(yenidusman)

    i += 1

for dusman in dusmanlar:
    dusman.print()
