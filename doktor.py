from personel import Personel

class Doktor(Personel):

    zam_orani = 1.1

    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def get_uzmanlik(self):
        return self.__uzmanlik
    
    def get_deneyim_yili(self):
        return self.__deneyim_yili
    
    def get_hastane(self):
        return self.__hastane
    
    def set_uzmanlik(self, uzmanlik):       #overwrite!
        self.__uzmanlik = uzmanlik
    
    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili
    
    def set_hastane(self, hastane):
        self.__hastane = hastane

    def maas_arttir(self):
        self.__maas = self.__maas * self.zam_orani

    def __str__(self):
        print("----- Doktor Bilgileri -----")
        print("Personel no: "+ self.get_personel_no())
        print("Ad: "+self.get_ad())
        print("Soyad: "+self.get_soyad())
        print("Departman: "+self.get_departman())
        print("Maas: "+self.get_maas())
        print("Uzmanlik: "+self.get_uzmanlik())
        print("Deneyim yili: "+self.get_deneyim_yili())
        print("Hastane: "+ self.get_hastane())
        print("------------------------------")