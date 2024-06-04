from personel import Personel

class Hemsire(Personel):

    zam_orani = 1.05

    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def get_calisma_saati(self):
        return self.__calisma_saati
    
    def get_sertifika(self):
        return self.__sertifika
    
    def get_hastane(self):
        return self.__hastane
    
    def set_calisma_saati(self, calisma_saati):                  #overwrite!
        self.__calisma_saati = calisma_saati
    
    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika

    def set_hastane(self, hastane):
        self.__hastane = hastane

    def maas_arttir(self):
        self.__maas = self.__maas * self.zam_orani

    def __str__(self):
        print("----- Hemsire Bilgileri -----")
        print("Personel no: "+ self.get_personel_no())
        print("Ad: "+self.get_ad())
        print("Soyad: "+self.get_soyad())
        print("Departman: "+self.get_departman())
        print("Maas: "+self.get_maas())
        print("Calisma saati: "+self.get_calisma_saati())
        print("Sertifika: "+self.get_sertifika())
        print("Hastane: "+ self.get_hastane())
        print("------------------------------")