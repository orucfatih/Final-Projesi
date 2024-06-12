from personel import Personel
from hemsire import Hemsire
from doktor import Doktor
from hasta import Hasta
import pandas as pd

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

def dataframe():
    tum_nesneler = personeller + doktorlar + hemsireler + hastalar 
    data = {'sinif': [type(obj).__name__ for obj in tum_nesneler],
    'personel_no': [obj.get_personel_no() if hasattr(obj, 'get_personel_no') else None for obj in tum_nesneler],
    'ad': [obj.get_ad() for obj in tum_nesneler],
    'soyad': [obj.get_soyad() for obj in tum_nesneler],
    'departman': [obj.get_departman() if hasattr(obj, 'get_departman') else None for obj in tum_nesneler],
    'maas': [obj.get_maas() if hasattr(obj, 'get_maas') else None for obj in tum_nesneler],
    'uzmanlik': [obj.get_uzmanlik() if hasattr(obj, 'get_uzmanlik') else None for obj in tum_nesneler],
    'deneyim_yili': [obj.get_deneyim_yili() if hasattr(obj, 'get_deneyim_yili') else None for obj in tum_nesneler],
    'hastane': [obj.get_hastane() if hasattr(obj, 'get_hastane') else None for obj in tum_nesneler],
    'calisma_saati': [obj.get_calisma_saati() if hasattr(obj, 'get_calisma_saati') else None for obj in tum_nesneler],
    'sertifika': [obj.get_sertifika() if hasattr(obj, 'get_sertifika') else None for obj in tum_nesneler],
    'hasta_no': [obj.get_hasta_no() if hasattr(obj, 'get_hasta_no') else None for obj in tum_nesneler],
    'dogum_tarihi': [obj.get_dogum_tarihi() if hasattr(obj, 'get_dogum_tarihi') else None for obj in tum_nesneler],
    'hastalik': [obj.get_hastalik() if hasattr(obj, 'get_hastalik') else None for obj in tum_nesneler],
    'tedavi': [obj.get_tedavi() if hasattr(obj, 'get_tedavi') else None for obj in tum_nesneler]}

    df = pd.DataFrame(data)
    df = df.fillna(0)
    print(df.to_string())
    

def main():
    while True:
        try:
            secenek = input("Ekleme icin 1\nGoruntuleme icin 2 \nDataFrame islemleri icin 3 tuslayiniz.\n(Cikmak icin 0 tuslayiniz.)")
            if secenek == "1":
                ekle()
            elif secenek =="2":
                goruntule()
            elif secenek == "3":
                dataframe()
            elif secenek == "0":
                print("Program sonlandiriliyor...")
                break
            else:
                print("Yanlis bir giris yaptiniz! Tekrar deneyin.")

        except ValueError:
            print("Yanlis bir giris yaptiniz! Tekrar deneyin.")

    
main()
