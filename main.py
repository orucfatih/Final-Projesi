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

def ekle():
    try:
        secenek = input("Personel eklemek icin 1\nDoktor eklemek icin 2\nHemsire eklemek icin 3\nHasta eklemek icin 4\nCikmak icin 0 tuslayiniz.")
        if secenek == "1":
            personel_ekle()
        elif secenek == "2":
            doktor_ekle()
        elif secenek == "3":
            hemsire_ekle()
        elif secenek == "4":
            hasta_ekle()
        elif secenek == "0":
            pass
        else:
            print("Yanlis bir giris yaptiniz! Tekrar deneyin.")
            ekle()
    except ValueError:
        print("Yanlis bir giris yaptiniz! Tekrar deneyin.")
        ekle()

def goruntule():
    try:
        secenek = input("Personel goruntulemek icin 1\nDoktor goruntulemek icin 2\nHemsire goruntulemek icin 3\nHasta goruntulemek icin 4\nCikmak icin 0 tuslayiniz.")
        if secenek == "1":
            if personeller == []:
                print("Personel bulunamadi.")
                goruntule()
            else:
                for personel in personeller:
                    print(personel)
        elif secenek == "2":
            if doktorlar == []:
                print("Doktor bulunamadi.")
                goruntule()
            else:
                for doktor in doktorlar:
                    print(doktor)
        elif secenek == "3":
            if hemsireler == []:
                print("Hemsire bulunamadi.")
                goruntule()
            else:
                for hemsire in hemsireler:
                    print(hemsire)
        elif secenek == "4":
            if hastalar == []:
                print("Hasta bulunamadi.")
                goruntule()
            else:
                for hasta in hastalar:
                    print(hasta)
        elif secenek == "0":
            pass
        else:
            print("Yanlis bir giris yaptiniz! Tekrar deneyin.")
            goruntule()
        
    except ValueError:
        print("Yanlis bir giris yaptiniz! Tekrar deneyin.")
        goruntule()

def main():
    while True:
        try:
            secenek = input("Ekleme icin 1\nGoruntuleme icin 2 tuslayiniz.\n(Cikmak icin 0 tuslayiniz.)")
            if secenek == "1":
                ekle()
            elif secenek =="2":
                goruntule()
            elif secenek == "0":
                print("Program sonlandiriliyor...")
                break
            else:
                print("Yanlis bir giris yaptiniz! Tekrar deneyin.")

        except ValueError:
            print("Yanlis bir giris yaptiniz! Tekrar deneyin.")

    
main()
