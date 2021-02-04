# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:20:38 2019

@author: gozdemihranaltinsoy
"""


sayi=10
sayi=10.2
sayi="Gözde"

sayi=int(input("Bir sayı girin:"))
print(sayi*2)
sayi2=eval(input("A:"))
print(sayi2%2) #sayi2 mod 2
metin=input("Kelime:")
print(metin*2)

ad=input("Adı:")
soyad=input("Soyadı:")
adsoyad=ad+" "+soyad
print(adsoyad)

print('Emir\'in bugün bilgisarı sorun çıkardı')
print("Emir\nKüçükaydın")
print("Emirhan\tKüçükaydın")
print("İrem\tElçin")

print(123,"\t",23,"\t\t",4556)
print(12323,"\t",3,"\t\t",4556111)
print(1231,"\t",2322333,"\t",456)

sayı=10
sayı2=15
sayı3=20
print("Sayı= {} {} {}".format(sayı,sayı2,sayı3))
print("Sayı= {2} {0} {1}".format(sayı,sayı2,sayı3))
print(sayı,sayı2,sayı3)
print(sayı,"\n",sayı2,sayı3)

liste=[4,"A",34.2]
print(liste)
print(liste[0])

x="A" in liste
print(x)
print("A" in liste)

if ("A" in liste):
    print("A değeri var")
else:
    print("A değeri yok")

if (4 in liste):
    print("4 değeri var")
else:
    print("4 değeri yok")
    
if (4 in liste):
    print(4*2)
else:
    print(5*2)

liste.append(5)
print(liste)
#Emir: listenin başına 5 değerini nasıl ekleriz
#Gözde: Listenin 3. elemanına 5 değerini nasıl ekleriz
#İrem: Listenin 3. ve 4. elemanlarının yerini nasıl değiştiririz

liste=[3,4,2]
#for i in range(1,6): #range son değerin 1 eksiğine kadar çalışır
#    liste.append(input("Değer:"))

liste[0]=5
print(liste)

kelime="istanbul"
#kelime[0]="İ" #string değerlerde herhangi bir karakter değiştirilemez
print(kelime[0])
kelime="İstanbul"
print(kelime)
print(kelime[0:4]) #0.karakterden itibaren 3.karaktere kadar
kelime="Gözde Altınsoy"
print(kelime[6:11])
print(kelime[6::2])
print(kelime[::3])
print(kelime[::-1])
#ö d A t n o
print(kelime[1:5:2],kelime[6::2])
