# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:20:04 2019

@author: Gözde Mihran Altınsoy
"""
#%%
liste=list() #liste list tipiyle atandı
liste=[] #boş bir liste oluşturuldu

liste=[10,5,"İstanbul",10.6,5,True,5,"10.01.2019","10/01/2019"]
print(liste[0])
print(liste[2])
print(liste[2][0])
print(liste[2][0:3])
print(liste[2][::-1])
print(liste)
liste.append(3)
print(liste)
print("5 miktarı:",liste.count(5))
liste.insert(0,15)
liste.insert(5,"Mecidiyeköy") #5.indekse bu değeri ekler
print(liste)
liste.pop() #indeks belirtmediğimizde son değer silinir
print(liste)
liste.pop(5) #5.indeksindeki değer silinir
print(liste)
liste.clear()
print(liste)
#Boş bir liste tanımlayalım
#Listenin içine 0 ile 70 arasında 5 değerinin katlarını  atayalım
#Listedeki 45 değerini silerim
#Listenin 7. değerine "İstanbul" değerini ekleyelim
#Listedeki eleman sayısını elemansayisi bir değişkende tutup bu değeri ekrana yazdıralım
listem=[]
for i in range(0,70,5):
    listem.append(i)
listem.insert(6,"İstanbul") #7. değerine "İstanbul" değerini ekler
print("45 değerinin indeksi:",listem.index(45)) #45 değerinin indeksini verir
indeks=listem.index(45) #45 değerinin indeksini indeks değişkeninde tutar
listem.pop(indeks) #indeks indisindeki değeri siler
listem.pop(listem.index(40)) #40 değerini siler
print(listem)
print("Listemdeki toplam eleman sayısı:",len(listem))

#Sözlük: Dictionary
sozluk={"bir":1,"iki":2,"üç":3,"dört":4}
print(sozluk.values())
print(sozluk.keys())
print(sozluk["bir"])
sozluk2={"kedi":"cat",1:"one","sarı":"yellow","doktor":"doctor"}
print(sozluk2["kedi"])
print(sozluk2.get("sarı"))
sozluk2["gitmek"]="go"
print(sozluk2)
sozluk2.pop("kedi")
print(sozluk2)

"""
Kullanıcı adı ve şifre değerlerini tutan bir sözlük tanımlayalım: user-123,password-pass,student-st
1) user 123456 olarak düzenleyelim
2) student anahtarını silerim
3) Sözlüğe admin-adm yapısını ekleyelim
4) user olan kullanıcının şifresini ekrana getirelim
"""
sifreler={"user":123,"password":"pass","student":"st"}
sifreler["user"]=123456
sifreler.pop("student")
sifreler["admin"]="adm"
print(sifreler)
print(sifreler.get("user"))

#%%
mevsimler={"yaz":["haziran","temmuz","ağustos"],"sonbahar":["eylül","ekim","kasım"]}
print(mevsimler["yaz"])
sözlükler={"sayılar":{"bir":1,"iki":2,"üç":3},"şehirler":{"İst":"İstanbul","Ank":"Ankara"}}
print(sözlükler["sayılar"]["bir"])
print(sözlükler["şehirler"]["İst"])

#demetler
demet=(1,2,3,4,5)
print(demet[0]) #demetler sadece okunabilir
#demet[0]=10 #bu satır hata verir. Çünkü demetler değiştirelemez sadece okunabilir
demet=("a","b","c","a")
print(demet)
print(demet.count("a"))

sözlük={"sayı":(1,2,3)}
print(sözlük["sayı"])

sözlük={"sayı":len(demet)}
print(sözlük)

print(mevsimler.items())

print("\nitems:")
for i in mevsimler.items():
    print(i)
    
print("\nitems 2:")
for i,j in mevsimler.items():
    print(i,j)

print("\nkeys:")
for i in mevsimler.keys():
    print(i)
    
print("\nvalues:")   
for i in mevsimler.values():
    print(i)