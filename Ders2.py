# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:39:26 2019

@author: gozdemihranaltinsoy
"""

a=10
b=4
toplam=a+b
fark=a-b
carpim=a*b
bolum=a/b
tambolum=a//b #tam kısmı alır
donusturme=int(a/b) #tam kısmı alır
kalan=a%b
print(toplam,fark,carpim,bolum,tambolum,donusturme,kalan)

a,b=5,3
print(a,b)
a,b=b,a
print(a,b)

"""
if (şart):
    doğruysa çalışacak adımlar
else:
    yanlışsa çalışacak adımlar
""" 

#Kullanıcının girdiği iki sayıdan büyük olanın küçük olan sayıya 
#bölümünden kalanı veren program

print(4**2) # ** Üst alma operatörü

a,b=int(input("Sayı1:")),int(input("Sayı2:"))
if (a>b):
    print(a%b)
else:
    print(b%a)

print(a**b)
print(b**a)

print("Sayının negatifi",-a)
print("Sayının negatifi",-b)
a=-a #Sayı negtif oldu
a=a*-1 #Sayı pozitif oldu
print("a",a)
print("b",b)

print(4+3*2/5)
print((4+3)*2/5)
#işlem öncelik sırası
#ilk parantez içi, sonra çarpma bölme, sonra da toplama çıkarma
#aynı işlem önceliği olan işlemlerde soldan sağa doğru yapar

kelime="İstanbul Mecidiyeköy"

kelime=input("Kelime:")

uzunluk=len(kelime)
print("Uzunluk:",uzunluk)
#Kelimenin uzunluğu kadar kelimeyi ekrana yazdırsın
for i in range(0,uzunluk): #uzunluk-1 son değer
    #range(uzunluk) şeklinde de tanımlanabilir
    print(i+1,kelime)

toplam=0
sayi=10
toplam=toplam+sayi
toplam+=sayi #toplam ve sayi değerini topla, toplam değerinin yeni değeri yap
#Eşit olmama durumu: !=


#Kullanıcıdan n değeri alınır, n değeri en fazla 10 olabilir
#Girilen n kadar değer toplanacak, 
#eğer kullanıcı 0 değerini girerse toplama işlemi durur
#Sonuç ekrana yazdırılır

toplam=0
n=int(input("n:"))
if (n<=10):
    for i in range(n):
        sayi=int(input("Sayı:"))
        if (sayi!=0):
            toplam+=sayi
        else:
            break
else:
    print("Sayı 10'dan küçük olmalı")
print("Toplam=",toplam)

#1'den 50'ye kadar olan sayılardan tek olanları ekrana yazdıralım
for i in range(1,51):
    if (i%2==1):
        print(i)
       
#Kullanıcının girdiği 5 değeri listeye ekleyelim
#Bu değerlerden tek ve çift olanların toplamlarını ekrana yazdırırım

sayılar=[]
ctoplam,ttoplam=0,0
for i in range(1,6):
    sayılar.append(int(input("{}.sayı:".format(i))))
print(sayılar)
for i in sayılar:
    if (i%2==0):
        ctoplam+=i
    else:
        ttoplam+=i
print("Çift:",ctoplam,"\nTek:",ttoplam)

a=10
b="İstanbul"
c=[1,2,3,4,5]
d=10.4;
e=(2,3,4,5)
f={1:"bir",2:"iki",3:"üç"}
g="10"
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

isim="ISTANBUL"
print("01","04",2019,sep="/")
print(5,"a",23.7,isim[5],isim[2:5],isim[5:],sep="\n")
print(isim[1::2])
print(isim[::-1])

#isim değişkeninin içindeki karakterlerden 
#sesli harfleri ekrana yazdıralım
sesli=["a","e","ı","i","o","ö","u","ü"]
isim2=isim.lower()
#sesli harfleri yazdırma:
print("Sesli harfler:")
for i in isim2: # i str değeri tutar
    #isim str değerinin içindeki değerleri i değişkeninde sırasıyla tutar
    if i in sesli: #sesli listesinin içinde i harfi var mı?
        print(i)
print("Sessiz harfler:")
for i in isim2: # i str değeri tutar
    #isim str değerinin içindeki değerleri i değişkeninde sırasıyla tutar
    if i in sesli: #sesli listesinin içinde i harfi var mı?
        x=0
    else:
        print(i)
print("Sessiz harfler:")
for i in isim2: # i str değeri tutar
    kontrol=True #sessiz harf
    #isim str değerinin içindeki değerleri i değişkeninde sırasıyla tutar
    for j in sesli:
        if (i==j):
            kontrol=False #sesli harf 
    if (kontrol):
        print(i)

#Girilen sayının asal olup olmadığını ekrana yazdıran program
#Asal sayı: 1 ve kendisi dışında böleni olmayan sayıdır.
#Bir sayı yarısından daha büyük sayıya bölünemez.
a=int(input("Sayı:"))
kontrol=True #İlk aşamada sayının asal olduğunu kabul ediyoruz
if (a<=1):
    kontrol=False
else:
    for i in range(2,int(a/2+1)):
        if (a%i==0):
            kontrol=False #Burada sayının asal olmadığını tespit ettik
            break #Döngüyü kırıyoruz. Tekrar bölünebiliyor mu diye bakmaya gerek yok
if (kontrol):
    print("Sayı asaldır")
else:
    print("Sayı asal değildir")

a=10.345
b=232.09374
c=1111.4564322
print("{:10.2f}\n{:10.2f}\n{:10.2f}".format(a,b,c))  
print("{:.1f}\n{:.1f}\n{:.1f}".format(a,b,c))   
print("{:5.0f}\n{:5.0f}\n{:5.0f}".format(a,b,c)) 
#5.0 değerinde 0 ondalık sayısını, 5 değeri ondalık değeri
#ve nokta dahil bu değer için ekranda ayıracağı karakter sayısı


isim=input("İsminizi giriniz:")
print(type(isim))
print(isim)
#isim[1]="o" #Bu kod syntax hatası verir
#str değerlerde herhangi bir karakter değiştirilemez

isim=list(isim)
isim[1]="o" #bu kod hatasız çalışır
#çünkü listelerde bir elemanın değeri değiştirilebilir
print(type(isim), isim)

isim=str(isim)
#Burada isim değeri list görünümüyle değişkene atandı
#Bunu eski haline nasıl çevirebiliriz?
print(type(isim))
print(isim)

liste=[3,5,7,9,11]
liste.append(13)
print(liste)
liste.pop() #listenin son değerini siler
print(liste)
liste.pop(3) #listenin 3.indeksindeki değeri siler (9)
print(liste)

#Ve:
a=10 #çift mi?
b=20 #çift mi?
#ikisi de çift ise ekrana çift yazdıralım
if (a%2==0 and b%2==0):
    print("Ve durumu çift")

#Veya:
a=10 #çift mi?
b=20 #çift mi?
#Herhangi biri çift ise ekrana çift yazdıralım
if (a%2==0 or b%2==0):
    print("Veya durumu çift")

#1 ile 30 arasındaki değerlerden oluşan bir liste tanımlayalım
#Bu değerlerden 2 veya 5'e bölünen sayıları listeden silerim
#Listeyi ekrana yazdıralım
liste=[] #boş bir liste tanımladık
for i in range(1,31):
    liste.append(i)
print(liste)
liste2=[]
for i in range(0,30):
    print(i, liste[i])
    #if (liste[i]%2==0 or liste[i]%5==0):
    #2'ye veya 5'e bölünmesi durumu 
    if (liste[i]%2!=0 and liste[i]%5!=0): 
    #2'ye ve 5'e bölünmemesi durumu
        liste2.append(liste[i])
print(liste2)

liste=[10,4,6,3,8,12]
liste.sort() #Küçükten büyüğe sıralar
print(liste)
liste.sort(reverse=True) #Büyükten küçüğe sıralar
print(liste)    

liste=["Kocaeli","Istanbul","Ankara","Izmir","Muğla","Adana"]
liste.sort() #A'dan Z'ye sıralar
print(liste)
liste.sort(reverse=True) #Z'den A'ya sıralar
print(liste)        

print(chr(65)) #ascii kodu verilen değerin karakterini verir
print(ord("A")) #verilen karakterin ascii kodunu verir
