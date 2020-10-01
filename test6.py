#Inheritance (kalıtım)
"""
class ogrenci ():
    def __init__(self, isim, sinif, numara, staj_parasi):

        self.isim = isim
        self.sinif = sinif
        self.numara = numara
        self.staj_parasi = staj_parasi

    def bilgilerigoster(self):
        print("Öğrencinin bilgileri gösteriliyor")
        print("İsim:", self.isim, "Sınıf:", self.sinif,
              "Numara:", self.numara, "Staj:", self.staj_parasi)

    def stajazamyap(self, zam_miktari):
        print("Staja zam yapıldı----")
        self.staj_parasi += zam_miktari

    def sinifdegistir(self, yeni_sinif):
        print("Sınıf değiştiriliyor....")
        self.sinif = yeni_sinif
 # kalıtım yapılan sınıfın fonksiyonlarını veya değişkenlerini super() fonksiyonu ile çekiyoruz


class Ogretmen(ogrenci):
    def __init__(self, isim, sinif, numara, staj_parasi, is_sayisi):
        print("Öğretmen sınıfının yapıcı fonksiyonu")
        super().__init__(isim, sinif, numara, staj_parasi)
        self.is_sayisi = is_sayisi  # ek özellik

    def bilgilerigoster(self):
        print("Öğretmen sınıfının bilgileri gösteriliyor")
        print("İsim:", self.isim, "Sınıf:", self.sinif, "Numara:", self.numara,
              "Staj parası:", self.staj_parasi, "İş sayısı:", self.is_sayisi)

    def issayisiartir(self, artir):
        print("İş sayısı artırılıyor")
        self.is_sayisi += artir


Ogretmen = Ogretmen("Mahmut", 4, 666, 2500, 20)
Ogretmen.bilgilerigoster()
Ogretmen.issayisiartir(10)
Ogretmen.bilgilerigoster()
"""


class ogrenci():
    def derscalis(self):
        print("öğrenci şu anda ders çalışıyor")


class calisan():
    def calis(self):
        print("personel şu anda çalısıyo")


class yazilimci(ogrenci, calisan):
    pass


yazilimci = yazilimci()
yazilimci.derscalis()
yazilimci.calis()
