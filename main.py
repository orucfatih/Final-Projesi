from personel import Personel
from hemsire import Hemsire
from doktor import Doktor
from hasta import Hasta

personeller = []
doktorlar = []
hemsireler = []
hastalar = []

def personel_ekle():
    try:
        personel_no = input("Personel no: ")
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        departman = input("Departman: ")
        maas = int(input("Maas: "))

    except ValueError:
        print("Yanlis bir giris yaptiniz! Tekrar deneyin.")
        personel_ekle()

    personel = Personel(personel_no, ad, soyad, departman, maas)
    personeller.append(personel)

def doktor_ekle():
    try:
        personel_no = input("Personel no: ")
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        departman = input("Departman: ")
        maas = int(input("Maas: "))
        uzmanlik = input("Uzmanlik: ")
        deneyim_yili = int(input("Deneyim yili: "))
        hastane = input("Hastane: ")

    except ValueError:
        print("Yanlis bir giris yaptiniz! Tekrar deneyin.")
        doktor_ekle()

    doktor = Doktor(personel_no, ad, soyad, departman, maas,uzmanlik, deneyim_yili, hastane)
    doktorlar.append(doktor)

def hemsire_ekle():
    try:
        personel_no = input("Personel no: ")
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        departman = input("Departman: ")
        maas = int(input("Maas: "))
        calisma_saati = int(input("Calisma saati: "))
        sertifika = input("Sertifika: ")
        hastane = input("Hastane: ")

    except ValueError:
        print("Yanlis bir giris yaptiniz! Tekrar deneyin.")
        hemsire_ekle()

    hemsire = Hemsire(personel_no, ad, soyad, departman, maas,calisma_saati,sertifika, hastane)
    hemsireler.append(hemsire)

def hasta_ekle():
    try:
        hasta_no = input("Hasta no: ")
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        dogum_tarihi = input("Dogum tarihi: ")
        hastalik = input("Hastalik: ")
        tedavi = input("Tedavi: ")

    except ValueError:
        print("Yanlis bir giris yaptiniz! Tekrar deneyin.")
        hasta_ekle()

    hasta = Hasta(hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi)
    hastalar.append(hasta)

def main():
    pass


    
    

