# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:31:47 2019

@author: Gözde Mihran Altınsoy
"""

def sayi(x):
    return x

sayi2=lambda x:x

print("F:",sayi(5))
print("L:",sayi2(5))


def kare(x):
    return x**2

kare2=lambda x:x**2

print("F:",kare(4))
print("L:",kare2(4))


def usalma(a,b):
    return pow(a,b)

usalma2=lambda a,b:pow(a,b)

print(usalma(5,3))
print(usalma2(5,3))

#Sayı negatifse -1 katını, pozitif ve sıfırsa karesini döndüren lambda

negpoz=lambda x:x*-1 if x<0 else x**2

print("5:",negpoz(5))
print("-5:",negpoz(-5))
print("0:",negpoz(0))

#sayı çiftse çift tekse tek yazdıran lambda

negpoz2=lambda x:print("çift") if x%2==0 else print("tek")

negpoz2(5)
negpoz2(-5)
negpoz2(0)
#negpoz2(int(input("Değer:")))

#iki sayının bölümünü hesaplayan lambda, eğer bölen sayı 0 ise sonuç 0 olsun ve ekrana yazdırsın

bol=lambda x,y:print("0") if y==0 else print("Bölüm:",x/y)

bol(5,0)
bol(15,2)

#%%
s1,s2=int(input("sayı 1:")),int(input("sayı 2:"))
print(s1/s2)

#Hata Yakalama
#%%
try:
    s1,s2=int(input("sayı 1:")),int(input("sayı 2:"))
    print(s1/s2)
except():
    print("Hatalı Giriş")

#%%
def kontrol():
    try:
        s1,s2=int(input("sayı 1:")),int(input("sayı 2:"))
        print(s1/s2)
    except:
        print("Hatalı Giriş")
        kontrol()
kontrol()

#%%
def kontrol():
    try:
        s1,s2=int(input("sayı 1:")),int(input("sayı 2:"))
        print(s1/s2)
    except ZeroDivisionError:
        print("Bir sayı sıfıra bölünemez")
        kontrol()
    except ValueError:
        print("Hatalı Giriş")
        kontrol()
kontrol()

#%%
try:
    print(2.5**1000)
except OverflowError:
    print("Sayı çok büyük. Taşma var.")

#%%
s1,s2=input("sayı 1:"),input("sayı 2:")
print(s1*s2) #TypeError: hatası oluştu

#%%
try:
    s1,s2=input("sayı 1:"),input("sayı 2:")
    print(s1*s2)
except TypeError:
    print("Type hatası oluştu")

#%%
isim="İstanbul"
print(isim)
liste=list(isim)
print(liste)
kelime="".join(liste)
print(kelime)

isim="İstanbul"
#print(isim)
liste=list(isim)
#print(liste)
kelime=""
for i in range(0,len(liste)):
    kelime+=liste[i]
    print(kelime)

#%%
liste=[10,5,2,6,8,7]
liste.sort() #küçükten büyüğe sıralama
print(liste)

#%%
liste=[10,5,2,6,8,7]
liste.sort(reverse=True) #büyükten küçüğe sıralama
print(liste)

#%%
liste=[10,5,2,6,8,7]
print("Sırasız liste\n",liste)
for i in range(0,len(liste)-1):
    for j in range(i+1,len(liste)):
        if (liste[i]>liste[j]):
            liste[i],liste[j]=liste[j],liste[i]
print("Küçükten büyüğe sıralı liste\n",liste)


liste=[10,5,2,6,8,7]
print("Sırasız liste\n",liste)
for i in range(0,len(liste)-1):
    for j in range(i+1,len(liste)):
        if (liste[i]<liste[j]):
            liste[i],liste[j]=liste[j],liste[i]
print("Büyükten küçüğe sıralı liste\n",liste)

#%%
#while döngüsü ile listenin içinde yer alan negatif sayıları çıkarıp yeni bir liste haline getirsen
irem=[5,6,-2,-5,-3,7,-6,5]
i=0
x=len(isim) #Bu şekilde tanımlanmamalı!

while i<len(irem): #uzunluğun dinamik olması gerekiyor
    #çünkü silince uzunluk değişiyor
    if irem[i]<0:
        irem.__delitem__(i)
    else:
        i+=1 
    #else içinde yazmamızın nedeni sildikten sonra o sildiğimiz değerin yerine gelen değeri de kontrol etmesi gerekiyor. Bu yüzden i değerini else bloğunun içine aldık
print(irem)


irem=[5,6,-2,4,-3,7,-6,5,7,-2,6,6,7]

#while ve for ile listenin içinde hangi değerden kaç tane olduğunun çıktısını versin


