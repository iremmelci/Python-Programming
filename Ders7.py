# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:12:56 2019

@author: Gözde Mihran Altınsoy
"""

#Modüller:

import random

x=random.randint(0,100)

#%%

import ilkmodulum
print(ilkmodulum.toplam(5,6))
print(ilkmodulum.karekok(25))
#print(ilkmodulum.toplamlarinkaresi())
print(ilkmodulum.liste)
ilkmodulum.liste.sort()
print(ilkmodulum.liste)
ilkmodulum.liste.sort(reverse=True)
print(ilkmodulum.liste)
print(help(ilkmodulum))
#%%
import math
print(help(math)) #Tüm açıklamalarla beraber modulün yardım penceresini getirir
print(dir(math)) #Sadece fonksiyonları getirir

#%%
from math import * #math modülünün tüm fonksiyonlarını projeye dahil eder
print(ceil(5.2)) #yukarı yuvarlar
print(floor(5.7)) #aşağı yuvarlar
print(factorial(5)) #faktöriyelini alır

#%%
from math import ceil,floor #sadece bu iki fonksiyonu projeye dahil eder
#print(factorial(5)) #Bu fonksiyon kullanılamaz

#%%
import math as matematik
print(int(matematik.pow(5,3)))
print(matematik.pi)
#print(math.pi) #Artık math modül ismi geçerli değil

#%%
#Soru 1. Math modülündeki fonksiyonları kullanarak bir hesap makinesi geliştirelim
#1.Yukarı yuvarla (ceil) 
#2.Aşağı yuvarla (floor) 
#3.Faktöriyel(factorial)
#4.Üs alma (pow) (2.değer istenecek)
#5.Karekök alma (sqrt)
#6.Çıkış

#Her menü ekrana gelmeden önce sleep(1) ile 1 sn. bekleyelim. Bunun için import time

import time
import math
while True:
    print("""
    1.Yukarı yuvarla
    2.Aşağı yuvarla 
    3.Faktöriyel
    4.Üs alma
    5.Karekök alma
    6.Çıkış""")
    secim=int(input("Seçiminiz:"))
    if secim==6:
        break
    elif secim<=6 and secim>0:
        sayi=eval(input("Sayı:"))
    
    if secim==1:
        print(math.ceil(sayi))
    elif secim==2:
        print(math.floor(sayi))
    elif secim==3:
        print(math.factorial(sayi))
    elif secim==4:
        us=int(input("Us:"))
        print(math.pow(sayi,us))
    elif secim==5:
        print(math.sqrt(sayi))
    else:
        print("Geçersiz değer")
    time.sleep(1)

#%%
#Soru 2. İki parametre alan toplama(s1,s2), çıkarma(s1,s2), çarpma(s1,s2) ve bölme(s1,s2)  fonksiyonlarına sahip (toplama, çıkarma, çarpma, bölme işlemlerini hesaplatan) dortislem isimli modül oluşturalım ve projemize import edip fonksiyonları test edelim

import dortislem
try:
    print(dortislem.bolme(5,2))
    print(dortislem.bolme(5,0))
except:
    print("Hatalı giriş")
print("2.deneme:")
try:
    print(dortislem.bolme(5,"a"))
except:
    print("Hatalı giriş")

#%%
#Kullanıcı geçerli bir değer girine kadar kullanıcıdan değer isteyelim
import dortislem    
while True:
    try:
        sayi1,sayi2=int(input("Sayı 1:")),int(input("Sayı 2:"))
        print(dortislem.bolme(sayi1,sayi2))
        break
    except:
        print("Hatalı Giriş")

#%%
#Bir modül oluşturalım. Modül adı: modulum
#1. Kendisine gönderilen sayının asal sayı olup olmadığını bulup asal ise True, asal değil ise False değerini döndüren fonksiyon (asal)
#2. 1 ile 100 arasındaki asal sayıları bir listede tutup bu listeyi geri döndüren fonksiyon (asalsayilar)
#import modulum



#Sayı tahmin oyunu
#5 sayı burada girilecek ve 2.fonk (kontrolet) ile tek tek kontrol edilecek
"""
Modul - sayitahmin
1. fonk (sayiuret)-> 10 tane 1 ile 30 arasında sayı üreten bir fonksiyon tanımlanacak
return rastgelesayilar list()
random.randint(1,30)

2. fonk (kontrolet)-> Kullanıcının girdiği 5 değer, bu üretilen 10 sayının içinde var mı kontrol etsin ve olanları bir listede tutsun. time ile 1 sn bekletip "Kontrol ediliyor" çıktısını verelim 
return esitolansayilar list()
time.sleep(1) -> 1 sn. bekler
for i in liste
    if i in rastgelesayilar
    
3. fonk (yazdir)-> Doğru bilmiş olduğu değerlerin listesini ekrana yazdırsın
print(kontrolet())
"""