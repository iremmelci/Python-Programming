# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:00:35 2019

@author: Gözde Mihran Altınsoy
"""


Cafe işletiyoruz
Çalışan
    Id int
    adi str
    yasi int
    maasi int
    cinsiyet str
    aktif bool
        __init__()
        durumguncelle() --> print(self.durum)
        goruntule()
        kayitguncelle()
        kayitekle()
Menu
    Id int
    adi str
    tur str --> sıcakicecek, sogukicecek, arasicaklar, anayemekler ...
Alt_Menu
    Menu_Id int
    Id
    adi str
    turu str
    cesitleri list
    ozellikleri list
    fiyati list
    malzemeler list
        __init__()
        urunekle()
        guncelle()
Musteri

class menu():
    def __init__(self,Id,adi,tur):
        self.Id=Id
        self.adi=adi
        self.tur=tur
class alt_menu():
    def __init__(self,menu_Id,Id,adi,tur):
        self.menu_Id=menu_Id
        self.Id=Id
        self.adi=adi
        self.tur=tur
        

