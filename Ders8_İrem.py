# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:42:05 2019

@author: ORİON


sözlük={1:"bir",2:"iki",3:"üç",4:"dört"}
print(sözlük.keys())
print(sözlük.values())

"""
class Araba():
    vitestürü="otomatik"
    renk="mavi"
    motorgücü=1.5
    çekiş="4 çeker"
    
araba1=Araba()

araba1.vitestürü="manuel"
print("araba1:",araba1.vitestürü)
araba1.renk="kırmızı"
print(araba1.renk)

araba2=Araba()
araba2.renk="sarı"
araba2.motorgücü=1.2
araba2.vitestürü="yarı otomatik"
araba2.çekiş="2 çeker"
print(araba2.motorgücü,araba2.renk,araba2.vitestürü,araba2.çekiş)

def ekranayazdır(nesne):
    print(nesne.çekiş)
    print(nesne.renk)
    print(nesne.motorgücü)
    print(nesne.vitestürü)

ekranayazdır(araba2)

class Çalışan():
    def __init__(self,isim,yaş,cinsiyet,ünvan):
        self.isim=isim
        self.yaş=yaş
        self.cinsiyet=cinsiyet
        self.ünvan=ünvan
        print("init fonk çalıştı")
    def görüntüle(self):
        #pass
        print(self.cinsiyet)
        print(self.isim)
        print(self.yaş)
        print(self.ünvan)
    
    def yazdır(self):
        print("""
adı:{}
yaşı:{}
cinsiyeti:{}
ünvanı:{}""".format(self.isim,self.yaş,self.cinsiyet,self.ünvan))
    def ünvangüncelle(self,ünvan):
        self.ünvan=ünvan
    def kayıtekle(self):
        self.isim=input("isim: ")
        self.yaş=int(input("yaşı: "))
        self.cinsiyet=input("cinsiyet: ")
        self.ünvan=input("ünvanı: ")
çalışan1=Çalışan("irem",21,"kadın","öğrenci")

çalışan1.görüntüle()

çalışan2=Çalışan("irem",21,"kadın","bilgi yok.")
çalışan2.görüntüle()
çalışan2.ünvangüncelle("öğretmen")
çalışan2.yazdır()



 






