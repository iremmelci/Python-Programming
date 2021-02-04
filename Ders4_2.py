# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:53:55 2019

@author: uby1
"""

#sayının karesini döndüren fonksiyon:
def kare():
    sayi=10
    #sayi=eval(input("sayı:"))
    return sayi**2 #pow(sayi,2) #sayi*sayi

#iki sayının toplamını döndüren fonksiyon:
def topla():
    sayi1=10
    sayi2=5
    return sayi1+sayi2

def topla2(s1,s2):
    return s1+s2

def topla3(s1,s2):
    print(s1+s2)
    
def topla4():
    print(4+2)

#İçinde 20 değerini tutan sayi değişkeninin 6'ya bölümünden kalanını ekrana yazdıran fonksiyon:
def kalan():
    sayi=20
    print(sayi%6)

#girilen bir sayının asal olup olmadığını bulan fonksiyon
#asal sayı: 1 ve kendisi dışında böleni olmayan sayıdır.
#asal olmayan sayılara 0, 1 ve negatif sayılar dahildir.
def asal():
    asal_durum=True
    sayi=int(input("Sayı:"))
    if sayi<2:
        asal_durum=False
    for i in range(2,sayi):
        if (sayi%i==0):
            asal_durum=False
            break
    if asal_durum:
        print("Sayı asal")
    else:
        print("Sayı asal değil")
        

#1 ile 1000 arasındaki tüm asal sayıları, miktarlarını ve toplamlarını ekrana yazdıralım
def asal2():
    sayac=0
    toplam=0
    for sayi in range(1,1001):
        asal_durum=True
        if sayi<2:
            asal_durum=False
        for i in range(2,sayi):
            if (sayi%i==0):
                asal_durum=False
                break
        if asal_durum:
            sayac+=1
            print(sayi)
            toplam+=sayi
    print("Asal Sayı Miktarı:",sayac)
    print("Toplam:",toplam)

#Girilen sayı negatifse ekrana "Negatif", pozitifse ekrana "Pozitif" yazdıran fonksiyon
#Pozitif ve negatif sayıların toplamını geri döndürelim (return)
def pn(s):
    if s<0:
        print("Negatif")
    elif s>0:
        print("Pozitif")


def main():
    print(kare())
    print(topla())
    print(topla2(5,2))
    topla3(4,5)
    topla4()
    kalan()
    #asal()
    asal2()
    #Girilen sayı sıfır olana kadar girilen sayıları pn fonksiyonuna gönderelim
    #Yani sıfır girine kadar yani sıfır girilmediği sürece pn fonksiyonu çalışacak
    sayi=1
    while sayi!=0:
        sayi=eval(input("Sayı:"))
        pn(sayi)
main()