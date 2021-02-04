# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:38:51 2019

@author: Gözde Mihran Altınsoy
"""
#%%
sozluk={1:"bir",2:"iki"}
print(sozluk.keys())
print(sozluk.values())

class Araba():
    vitesturu="otomatik"
    renk="mavi"
    motor="1.5 ddi"
    cekis="4 çeker"

araba1=Araba()
print(araba1)
print(araba1.vitesturu)
print(Araba.vitesturu)

araba1.vitesturu="manuel"
print("Araba1:",araba1.vitesturu)
print("Araba:",Araba.vitesturu)

araba1.renk="Kırmızı"
print(araba1.renk)

Araba.renk="Mor"
#Rengi sarı olan , yarı otomatik vitesli, motor 1.2 ddi ve 2 çeker bir araba2 objesini Araba nesnesinden türetelim
araba2=Araba()
araba2.cekis="2 çeker"
araba2.motor="1.2 ddi"
araba2.renk="sarı"
araba2.vitesturu="yarı otomatik"

Araba.renk="Mor"
araba3=Araba() 

print(araba2.cekis,araba2.motor,araba2.renk,araba2.vitesturu)

def ekranayazdir(nesne):
    print(nesne.cekis)
    print(nesne.motor)
    print(nesne.renk)
    print(nesne.vitesturu)
    

print("\nAraba")
ekranayazdir(Araba)

print("\naraba2")
ekranayazdir(araba2)

print("\naraba3")
ekranayazdir(araba3)

araba4=Araba()
print("\naraba4")
ekranayazdir(araba4)

#%%
class Calisan():
    def __init__(self):
        self.isim=""
        self.yasi=0
        self.cinsiyet=""
        self.unvan=""
        print("init fonksiyonu çalıştı")
    def goruntule():
        pass

print(Calisan)
calisan1=Calisan()
print(calisan1.yasi)

#%%
class Calisan():
    def __init__(self,isim,yas,cinsiyet,unvan):
        self.isim=isim
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.unvan=unvan
        print("init fonksiyonu çalıştı")
    def goruntule(self):
        #pass
        print(self.isim)
        print(self.yas)
        print(self.cinsiyet)
        print(self.unvan)
    def yazdir(self):
        print("""
Adı      : {}
Yaşı     : {}
Cinsiyeti: {}
Unvanı   : {}""".format(self.isim,self.yas,self.cinsiyet,self.unvan))
    def unvan_guncelle(self,unvani):
        self.unvan=unvani
    def kayıt_güncelle(self,isim,yas,cinsiyet,unvan):
        self.isim=isim
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.unvan=unvan
    def kayıt_ekle(self):
        #pass
        self.isim=input("İsim:")
        self.yas=int(input("Yaş:"))
        self.cinsiyet=input("Cinsiyet:")
        self.unvan=input("Unvan:")
        """
        i=input("İsim:")
        y=int(input("Yaş:"))
        c=input("Cinsiyet:")
        u=input("Unvan:")
        return i,y,c,u
        """
calisan1=Calisan("Gözde",31,"K","Akademisyen")
calisan2=Calisan(isim="Emir",yas=20,cinsiyet="E",unvan="Bilgi yok")
print("calisan1")
calisan1.goruntule()
print("calisan2")
calisan2.goruntule()
print("calisan1")
calisan1.yazdir()

calisan2.unvan_guncelle("Mühendis")
print("calisan2")
calisan2.yazdir()

calisan3=Calisan("İrem",21,"K","Öğrenci")
calisan3.yazdir()
calisan3.unvan_guncelle("İçişleri Bakanı")
calisan3.yazdir()

calisan1.kayıt_güncelle("Emin",31,"E","Müdür")
calisan1.yazdir()

calisan4=Calisan("",0,"","")
calisan4.kayıt_ekle()
#calisan4.Calisan().kayıt_ekle()
calisan4.yazdir()