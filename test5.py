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
