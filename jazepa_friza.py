import itertools
import datetime
from datetime import time

class Pakalpojums:
    
    Pakalpojuma_kategorija =""
    Pakalpojuma_nosaukums =""
    Pakalpojuma_atlaide =""
    Pakalpojuma_cena =0 


    id_iter= itertools.count()
    def __init__(self,pak_kat=None,pak_nos=None,pak_atl=None,pak_cena=10):
        self.pakalpojumaId=next(self.id_iter)+1
        self.pakalpojumaKategorija=pak_kat
        self.pakalpojumaNosaukums=pak_nos
        self.pakalpojumaAtlaide=pak_atl
        self.pakalpojumaCenaStunda=pak_cena
        self.laiksPieejams=True
    
    def __repr__(self):
        if self.pakalpojumaKategorija: return self.pak_kat
        elif self.pakalpojumaNosaukums: return self.pak_nos
        elif self.pakalpojumaAtlaide: return self.pak_atl
        elif self.pakalpojumaCenaStunda: return self.pak_cena
        return''
    
    def Pakalpojuma_info(self):
        return [
            self.pakalpojumaKategorija,self.pakalpojumaNosaukums,
            self.pakalpojumaAtlaide,self.pakalpojumaCenaStunda
        ]
    
    def Pakalpojuma_info_print(self):
        print("Pakalpojuma kategorija: "+ str(self.pakalpojumaKategorija))
        print("Pakalpojuma nosaukums: " + str(self.pakalpojumaNosaukums))
        print("Pakalpojuma atlaide: "+ str(self.pakalpojumaAtlaide))
        print("Pakalpojuma cena par stundu: " + str(self.pakalpojumaCenaStunda))
        print("Laiks pieejams: " + str(self.laiksPieejams) + "\n")

class Klients:
    Klienta_vaards=""
    Klienta_uzvaards=""
    Klienta_PK=""
    Klienta_tel_numurs=""
    
    id_iter_kl = itertools.count()

    def __init__(self,_vaards,_uzvaards,_pk,_tel_numurs):
        self.Klienta_id = next(self.id_iter_kl) + 1
        self.Klienta_vaards=_vaards
        self.Klienta_uzvaards=_uzvaards
        self.Klienta_PK=_pk
        self.Klienta_tel_numurs=_tel_numurs

    def Klienta_info(self):
        print("Klienta vards:"+ self.Klienta_vaards)
        print("Klienta uzvards:"+self.Klienta_uzvaards)
        print("Klienta personas kods:"+self.Klienta_PK)
        print("Klienta telefona numurs:"+self.Klienta_tel_numurs)

    def Klientu_info_print(self):
        print("Klienta vārds: "+ str(self.Klienta_vaards))
        print("Klienta uzvārds: " + str(self.Klienta_uzvaards))
        print("Klienta personas kods : "+ str(self.Klienta_PK))
        print("Klienta Tel. numurs : " + str(self.Klienta_tel_numurs)) 

class Izmantosana:
    Pakalpojuma_saakuma_laiks= 0
    Pakalpojuma_beigu_laiks=0
    Pakalpojuma_datums=0
    Izmantosdana_cena_stunda=10
    id_pakalpojums=0
    id_klients=0
    Izmantosana_id=0

    id_iter_izmantosana= itertools.count()

    def Cena_kopa(self):
        kopeja_cena=self.Izmantosdana_cena_stunda*(((self.Pakalpojuma_beigu_laiks - self.Pakalpojuma_saakuma_laiks)))
        return kopeja_cena
    
    def Izmantosana_info_print(self):
        print("Pakalpojuma sakuma laiks:"+ str(self.Pakalpojuma_saakuma_laiks))
        print("Pakalpojuma beigu laiks:"+ str(self.Pakalpojuma_beigu_laiks))
        print("Pakalpojums id:"+ str(self.id_pakalpojums))
        print("Klients id:"+ str(self.id_klients))
        print("Pakalpojuma cena stunda, EUR:"+str(self.Izmantosdana_cena_stunda)+"\n")

kli1=Klients("Paša","Tehnik","041203-21423","34277823")
kli1=Klients("Gleb","Arakazjan","121203-12239","26912412")
kli1=Klients("Abdul","Ahmed","121179-12364","23453789")

pak1=Pakalpojums("Matu griezšana","PieManis","20%","15")
pak2=Pakalpojums("Uzacu un skropstu krāsošana ","Uzacu krāsošana ","25%")
pak3=Pakalpojums("Kosmētikas procedūras ","Higiēniskā sejas tīrīšana ","25%")

print(pak1.pakalpojumaId)
pak1.Pakalpojuma_info()
pak1.Pakalpojuma_info_print()
print(pak2.pakalpojumaId)
pak2.Pakalpojuma_info()
pak2.Pakalpojuma_info_print()
print(pak3.pakalpojumaId)
pak3.Pakalpojuma_info()
pak3.Pakalpojuma_info_print() 

print(kli1.Klienta_id)
kli1.Klienta_info()
kli1.Klientu_info_print()
print(kli1.Klienta_id)
kli1.Klienta_info()
kli1.Klientu_info_print()
print(kli1.Klienta_id)
kli1.Klienta_info()
kli1.Klientu_info_print()