import itertools
import datetime
from datetime import time

class Pakalopojums:
    Pakalopojuma_kategorija=""
    Pakalopojuma_nosaukums=""
    Pakalopojuma_atlaide=""
    Pakalopojuma_cena=0

    id_iter = itertools.count()

    def __init__(self,pak_kat=None,pak_nos=None,pak_atl=None,pak_cena=10):
        self.Pakalpojuma_id=next(self.id_iter)+1
        self.Pakalpojuma_kategorija=pak_kat
        self.Pakalpojuma_nosaukums=pak_nos
        self.Pakalpojuma_atlaide=pak_atl
        self.Pakalpojuma_cena_stunda=pak_cena
        self.Laiks_pieejams=True
        print("Pakalpojuma kategorija: "+str(self.Pakalopojuma_kategorija))

    def __repr__(self):
        if self.Pakalopojuma_kategorija: return self.pak_kat
        elif self.Pakalopojuma_nosaukums: return self.pak_nos
        elif self.Pakalopojuma_atlaide: return self.pak_atl
        elif self.Pakalpojuma_cena_stunda: return self.pak_cena
        return ''
    def Pakapojuma_info(self):
        return[self.Pakalopojuma_kategorija,self.Pakalopojuma_nosaukums,
               self.Pakalopojuma_atlaide,self.Pakalpojuma_cena_stunda]
    def Pakalpojuma_info_print(self):
        print("Pakalpojuma kategorija: "+str(self.Pakalopojuma_kategorija))
        print("Pakalpojuma nasaukums: "+ str(self.Pakalopojuma_nosaukums))
        print("Pakalpojuma atlaide: "+ str(self.Pakalopojuma_atlaide))
        print("Pakalpojuma cena par stundu: "+str(self.Pakalpojuma_cena_stunda))
        print("Laiks pieejams: "+str(self.Laiks_pieejams)+"\n")

pak1=Pakalopojums("Frizētāva","Matu griešāna","20%",30)
pak2=Pakalopojums("Uzacu un skrostu krāsošāna","Uzacu krāsošana","25%")
pak3=Pakalopojums("Kosmētiskās procedūras","Higiēniska sajas tīrīšana")
print(pak1.Pakalpojuma_id)
pak1.Pakapojuma_info()
pak1.Pakalpojuma_info_print()
print(pak2.Pakalpojuma_id)
pak2.Pakapojuma_info()
pak2.Pakalpojuma_info_print()
print(pak3.Pakalpojuma_id)
pak3.Pakapojuma_info()
pak3.Pakalpojuma_info_print()