"""
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
"""


import sqlite3
import random
import time
import datetime

con = sqlite3.connect("dersler.db")

cursor = con.cursor()


def tabloolustur():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Tablo1 (zaman Real,tarih Text,anahtarkelime Text,deger Real)")


def rastgeledegerekle():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(
        zaman).strftime('%Y-%m-%D $H:$M:$S'))
    anahtarkelime = "Python3 Sqlite"
    deger = random.randrange(0, 5)
    cursor.execute("INSERT INTO Tablo1 (zaman,tarih,anahtarkelime,deger) VALUES (?,?,?,?)",
                   (zaman, tarih, anahtarkelime, deger))
    con.commit()


tabloolustur()
i = 0
while (i < 5):
    rastgeledegerekle()
    time.sleep(1)
    i += 1
con.close()


def degerlerial():
    cursor.execute("SELECT * FROM Tablo1 Where deger = 2.0")

    data = cursor.fetchall()
    for i in data:
        print(i)


degerlerial()
tabloolustur()
