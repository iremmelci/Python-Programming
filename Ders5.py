# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:13:09 2019

@author: Gözde Mihran Altınsoy
"""
"""
ÖDEV:
        *
       ***
      *****
     *******
    *********
   ***********
  *************
 ***************
*****************
"""
#Baş. değeri: 1 
#2'şer 2'şer yıldızlar artıyor
#8 boşluk bırak
#1'er 1'er azalıyor
#%%
sayac=8
for i in range(0,9,1):
    print(" "*sayac,end="")
    sayac-=1
    for j in range(0,i*2+1):
        print("*",end="")
    print()

satir=int(input("Kaç kere tekrar edecek...:"))
sayac=satir-1
for i in range(0,satir,1):
    print(" "*sayac,end="")
    sayac-=1
    for j in range(0,i*2+1):
        print("*",end="")
    print()
#%%
"""
ÖDEV
#Kare oluşturma:
***
* *
***

*****
*   *
*   *
*   *
*****
5 girdiğinde;
5 yıldız çiz
alt satıra geç
* 5-2 boşluk * çiz alt satıra geç 5-2 kez tekrar et
alt satıra geç
5 yıldız çiz

"""
#%%
sayi=int(input("Uzunluk sayısı..:"))

print("\n1.yöntem")

print("*"*sayi)
for i in range(1,sayi-1):
    print("*"," "*(sayi-4),"*")
print("*"*sayi)

print("\n2.yöntem")

for i in range(1,sayi+1):
    if i==1 or i==sayi:
        print("*"*sayi)
    else:
        print("*"," "*(sayi-4),"*")


#%%
"""
ÖDEV
*
 **
  ***
   ****
"""
sayi=int(input("Uzunluk sayısı..:"))
for i in range(1,sayi+1):
    print(" "*(i-1),"*"*i)

#%%
def emirhan():
    for i in range(5): #i 0'dan 4'e kadar gider
        print("Emirhan")

def irem(x):
#metoddan gelen değer kadar ekrana yazdıracak
    for i in range(x):
        print(i+1,".İrem")
    
def gozde():
#girilen sayı kadar ekrana yazdıracak
    sayi=int(input("Sayı:"))
    for i in range(sayi):
        print("Gözde")
    
def ige():
#girilen sayı kadar ekrana metni yazdıracak ve sayıyı return edecek (geri döndürecek)
    sayi=int(input("Sayı:"))
    for i in range(sayi):
        print("İGE")
    return sayi

def sayiyaz(s1,s2):
#gelen metottaki girilen iki sayı arasındaki sayıları ekrana yazdıracak ve sayıların farkını return edecek (geri döndürecek)
    if s1>s2:
        s1,s2=s2,s1
    for i in range(s1,s2+1):
        print(i)
    return s2-s1

#girilen kelimenin karakter sayısı çift ise kelimenin bütün karakterlerini büyük harfe dönüştürsün, tek ise karakterlerini 2'şer 2'şer atlayarak ekrana yazdırsın
#Ör. kelime İstanbul 8 karakter yani çift
#ekrana İSTANBUL yazdıracak
#Ör. kelime Mecidiyeköy 11 karakter yani tek
#ekrana Mcdyky

#bir sayının çarpanlarını ve çarpanlarının miktarını bulan fonksiyon (o sayıya tam bölünen sayıları)


#bir sayının asal çarpanları bulan fonksiyon
#bir sayı asal mı?
def asal_carpan():
    sayi=int(input("Sayi:"))
    for i in range(2,sayi):
        if (sayi%i==0):
            #i asal mı? Asal ise yaz
            asal=True
            for j in range(2,i):
                if (i%j==0):
                    asal=False
            if (asal):
                print(i)
asal_carpan()

#Ödev-2
#1 ile 20 arasındaki sayıların asal çarpanlarını tek tek ekrana  yazdıran 


"""
emirhan()
irem(10)
gozde()
x=ige()
print(x)  
#print(ige())
  
print("Fark:",sayiyaz(3,10))
"""