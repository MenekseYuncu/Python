# print('menekse' + ' Hello ' + 'world')
# print("Karakter Kaydetme Programı")

"""
ad = input("Karakterin adi :")
soyad = input("Karakterin soyadi :")
takimi = input("Karakterin takimi :")

bilgiler = [ad,soyad,takimi]

print("Database'e kaydediliyor....")

print("Karakterin adi: {}\nKarakterin soyadi: {}\n Karakterin takimi: {}".format(
    bilgiler[0],bilgiler[1],bilgiler[2]))

print("kaydedildi...")
"""

"""
note = float(input("Not Ortalamanizi Giriniz:"))

if note >= 90:
    print("Takdir aldiniz!")

elif note >= 70:
    print("Tesekkur aldiniz!")

else:
    print("Kaldiniz!")  """


"""
# Kullanıcı İsmi ve Parola Kontrolü

defkullanici = "Mahmut"
defparola = "1234"

Kullanıcı = input("Kullanıcı Adı:")
Parola = input("Parola:")
if((defkullanici == Kullanıcı) and (defparola == Parola)):
    print("Siteye Hoş Geldiniz")
elif((defkullanici!=Kullanıcı) and (defparola == Parola)):
    print("Kullanıcı Adınızı Yanlış Girdiniz")
elif((defkullanici == Kullanıcı) and (defparola != Parola)):
    print("Şifrenizi mi Unuttunuz")
else:
    print("TEKRAR DENEYİNİZ")   """


"""
# while döngüsü

defkullanici = "efe"
defparola = "1234"

while(True):
    Kullanıcı = input("Kullanıcı Adınızı Girin:")
    Parola = input("Parolanızı Giriniz:")

    if((defkullanici == Kullanıcı.lower()) and (defparola == Parola)):
        print("Hoşgeldiniz")
        break
    elif((defkullanici != Kullanıcı) and (defparola == Parola)):
        print("Kullanıcı Adınız Hatalı")
    elif((defkullanici == Kullanıcı) and (defparola != Parola)):
        print("Şifreniz Hatalı")
        print("Şifrenizi Yenilemek İstermisiniz? (E/H)")

        cevap = input()
        if(cevap == "E"):
            yeniparola = input("Yeni Parola:")
            print("Lütfen Bekleyiniz")
            defparola = yeniparola
            print("Şifre Başarıyla Değişti")
    else:
        print("Tekrar Deneyin")           """

"""
for i in range(10):
    print(i*"*") """

"""

print("Hoşgeldiniz")

def toplama (a,b):
    return(a+b)

def cikarma (a,b):
    return(a-b)

def carpma (a,b):
    return(a*b)

def bolme (a,b):
    ab = a/b
    return(" : {:.5f}".format(ab))


print("Yapılacak İşlemi Seçiniz:")
print("=========================")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

secim = input("Seçiminiz (1/2/3/4):")

sayi1 = int(input("1.Sayı:"))
sayi2 = int(input("2.Sayı:"))

if (secim == "1"):
    print(sayi1,"+",sayi2,"=",toplama(sayi1,sayi2))

elif (secim == "2"):
    print(sayi1,"-",sayi2,"=",cikarma(sayi1,sayi2))

elif (secim == "3"):
    print(sayi1,"*",sayi2,"=",carpma(sayi1,sayi2))

elif (secim == "4"):
    print(sayi1,"/",sayi2,"=",bolme(sayi1,sayi2))

else:
    breakpoint  """

"""

def faktoriyel (numara):
    faktoriyel=1
    for i in range (1,numara+1):
        faktoriyel*=i
    print("faktoriyel:",faktoriyel)


sayi = int(input("Sayıyı Giriniz:"))

faktoriyel(sayi)
faktoriyel(7)   """

"""
def kayıt_ekle(ad="bilgi yok",soyad="bilgi yok",yas="bilgi yok",sehir="bilgi yok",meslek="bilgi yok"):
    print("Kayıt Ekleniyor")
    print("Ad:{}\n Soyad:{}\n Yas:{}\n Sehir:{}\n Meslek:{}\n".format (
        ad,soyad,yas,sehir,meslek))
    print("Kayıt Başarıyla Eklendi")


kayıt_ekle(ad="Menekşe",soyad="Yüncü",yas="20",sehir="Mersin",meslek="pc")    """


"""
def printer(sekil):
    geometri(sekil)

def geometri(sekil):
    print(sekil)
    if (len(sekil) == 3):
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]

        if (a+b) > c and (a+c) > b and (b+c) > a:
            if a == b == c:
                print("Eşkenar Üçgen")
            elif (a == b) or (a == c) or (b == c):
                print("İkiz Kenar Üçgen")
            else:
                print("Çeşit Kenar Üçgen")
        else:
            print("Üçgen Belirtilmiyor")     
    elif len(sekil) == 4:
        a = sekil[0]
        b = sekil[1]   
        c = sekil[2]
        d = sekil[3]   
        if (a == b) and (b == c) and (c == d):
            print("Kare")
        elif (a == c) and (b == d):
            print("Dikdörtgen")
        else:
            print("Normal Dörtgen") 
    else:
        print('yeyeyey')

while (True):
    eleman_sayisi = int(input("Eleman Sayısı:"))

    if(eleman_sayisi == 3):
        a = int(input("A:"))
        b = int(input("B:"))
        c = int(input("C:"))
        sekil = [a,b,c]
        printer(sekil)
        #geometri: ([a,b,c])

    elif(eleman_sayisi == 4):
        a = int(input("A:"))
        b = int(input("B:"))
        c = int(input("C:"))
        d = int(input("D:"))
        printer([a,b,c,d])
        #geometri:([a,b,c,d])
    else:
        print('try lan bir daha ')
"""
print('30f66ec9b0b1bfcf853ea11c3ae3f1602a638581')
