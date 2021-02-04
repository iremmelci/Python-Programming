# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:34:05 2019

@author: Gözde Mihran Altınsoy
"""
#%%
kelime="İstanbul"
print(kelime[0:3])
print(kelime[2:5])

sayi=10.567
sayi2=1245
print("{:5.1f}\n{:5}".format(sayi,sayi2))
#%%
#şartlı ifade: if
#girilen yaş 10'dan küçükse çocuk, 18'den küçükse genç, 30'dan küçükse yetişkin, değilse yaşlı yazdıralım
#%%
yas=int(input("Yaşınızı girin..:"))
if yas<10:
    print("Çocuk")
elif yas<18:
    print("Genç")
elif yas<30:
    print("Yetişkin")
else:
    print("Yaşlı")
#%%
#Girilen metnin karakter sayısı 5'den küçük eşitse ekrana karakter sayısının 2 katını, 10'dan küçükse karakter sayısının karesi, değilse karakter sayısı kadar ekrana metni yazdıran program
#%%
kelime=input("Kelime:")
uzunluk=len(kelime)
if uzunluk<=5:
    print(uzunluk*2)
elif uzunluk<10:
    print(uzunluk**2) #print(pow(uzunluk,2))
else:
    print(kelime*uzunluk)
#%%    
#Hava sıcaklığını alalım. Sıcaklık -10 ile 0 arasında ise "Dondurucu soğuk", 10 ile 20 arasında ise normal, 30 ile 40 "Bunaltıcı sıcak", diğerlerinde ise "Diğer durum" yazdırsın



#1 ile 50 arasındaki sayıları arasında tab boşluğu bırakarak yanyana ekrana yazdıralım
#%% 
for i in range(1,51):
    print(i,"\t",end="") 
#end="" ifadesi alt satıra geçmemesini sağlar

#%% 
#11 ile 25 arasındaki tek sayıları alt alta ekrana yazdıralım
for i in range(11,26,2):
    print(i) 
#%%  
for i in range(11,26):
    if i%2!=0:
        print(i) 
#10 ile 50 arasındaki 5'in katı olan sayıları alt alta ekrana yazdıralım
#%% 
for i in range(10,51):
    if i%5==0:
        print(i) 
#%% 
for i in range(10,51,5):
    print(i) 
#1 ile 100 arasındaki çift sayıları ve karelerini alt alta ekrana yazdıralım

#%% 
for i in range(2,101,2):
    print(i,i**2) 
    
#%%    
for i in range(1,101):
    if i%2==0:
        print(i,i**2) 
#%%
#girilen iki sayının arasındaki tüm 2 veya 5'e bölünenlerin toplamını ve bu şarta uyan sayı miktarını ekrana yazdıralım
s1=int(input("Sayı1:"))
s2=int(input("Sayı2:"))
if s1>s2:
    s1,s2=s2,s1 #yer değiştirme gerçekleşiyor
#Diğer programlama dillerinde değişkenler arasında yer değiştirmek için aşağıdaki yapıyı kullanmak zorunda kalıyorduk. Ama Python'da bu tek satırda gerçekleşiyor. s1,s2=s2,s1
    #bos=s1
    #s1=s2
    #s2=bos
toplam=0
sayac=0
sayilar=[] #sayilar=list()
for i in range(s1,s2+1):
    if i%2==0 or i%5==0:
        toplam+=i #toplam=toplam+i
        sayac+=1
        sayilar.append(i)
print(sayilar)
print("Toplam:",toplam,"\nSayaç:",sayac)
print("Toplam:",sum(sayilar),"\nSayaç:",len(sayilar))
#%%
#Girilen sayının faktöriyelini hesaplayalım
#5 girilirse; sonuc=1*2*3*4*5 veya sonuc=5*4*3*2*1
sayi=int(input("Sayı girin..:"))
sonuc=1
for i in range(1,sayi+1):
    sonuc*=i
print("Sonuç:",sonuc)

#%%
#2'ler Çarpım tablosunu ekrana yazdıralım
for i in range(1,11):
    print(2,"*",i,"=",2*i)
#%%
#Çarpım tablosunu ekrana yazdıralım
for i in range(1,11):
    for j in range(1,6):
        print(i,"*",j,"=",i*j,"\t",end="")
    print("\n",end="")
#%%
#Fibonacci serisi oluşturalım ve listede tutalım
#1 1 2 3 5 8 13 21 34 55
#Fibonacci serisinin 10. değerini bulalım
fib=[]
fib.append(1)
fib.append(1)
print(fib)
#Aşağıdaki adımları gerçekleştiren döngü yapısını kuralım
"""
fib.append(fib[0]+fib[1])
print(fib)
fib.append(fib[1]+fib[2])
print(fib)
fib.append(fib[2]+fib[3])
print(fib)
"""
for i in range(1,9):
    fib.append(fib[i-1]+fib[i])
print(fib)
print(fib[len(fib)-1])
print(fib[9])
#%%
while True:
    #Sonsuz döngü
    break

#%%
#Kullanıcı negatif sayı girene kadar (kullanıcı pozitif sayı veya sıfır girdiği sürece) değer alıp bu değerleri listede tutalım
x=[]
while True:
    x.append(int(input("Sayı:")))
    if x[len(x)-1]<0:
        break

#%%
#Kullacı çift sayı girdiği sürece çalışan döngü yazınız
while True:
    y=int(input("Sayı:"))
    if y%2!=0:
        break
    
#%%
#Kullanıcı çift sayı girdiği sürece çalışan döngü yazınız
sayi=2 #çift sayı tanımladık
while sayi%2==0:
    sayi=int(input("Sayı:"))
    
#%%
#Kullanıcı sıfır girene kadar girdiği değerlerin toplamını hesaplayan program

#%%
#Kullanıcı sıfır girene kadar girdiği pozitif ve negatif değerleri ekrana yazdıralım 
#Bir listede tutarak ekrana yazdırabiliriz

#%%
#1 ile 50 arasındaki sayıları while döngüsü ile ekrana yazdıralım

#Kullanıcı negatif sayı girine kadar girdiği sayı kadar ekrana * koyalım
"""
4: 
    *
    **
    ***
    ****
5:
    *
    **
    ***
    ****
    *****
"""
for i in range(5): # i değeri 0 ile 4 arasında değer alır. Yani for döngüsü 5 kere çalışır
    print(i,"G")
"""
4: 
    *
    **
    ***
    ****
    ***
    **
    *
    
"""

"""
ÖDEV
#Kare oluşturma:
***
* *
***
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
