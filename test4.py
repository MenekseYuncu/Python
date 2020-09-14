# sqlite veri tabanı
import sqlite3

con = sqlite3.connect("dersler.db")

cursor = con.cursor()


def tabloolustur():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ogrenciler (Ad TEXT,Soyad TEXT,Numara INT,DersNotu INT)")


def degerekle():
    cursor.execute(
        "INSERT INTO ogrenciler VALUES('Menekşe','Yüncü','666','85')")
    con.commit()
    con.close()


tabloolustur()
degerekle()
