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
"""


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
