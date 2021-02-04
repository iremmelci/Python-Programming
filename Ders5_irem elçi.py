# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:33:58 2019

@author: 303UBY00


kelime="istanbul"
print(kelime[0:3])
print(kelime[2:5])

sayi=10.56

yaş=int(input("yaşınızı giriniz: "))
if yaş<10:
    print("çocuk")
elif yaş<18:
    print("genç")
elif yaş<30:
    print("yetişkin")
else:
    print("yaşlı")
    
kelime=input("kelimeyi giriniz:")
uzunluk=len(kelime)
if(uzunluk<=5):
    print(uzunluk*2)
elif(uzunluk<=10):
    print(uzunluk**2)
else:
    print(kelime*uzunluk)
    
    
sıcaklık=int(input("hava sıcaklığını yazınız:"))
if(sıcaklık>-10 and sıcaklık<0):
    print("dondurucu soğuk")
elif(sıcaklık>10 and sıcaklık<20):
    print("normal")
elif(sıcaklık>30 and sıcaklık<40):
    print("bunaltıcı sıcak")
else:
    print("diğer durunmlar")
    
for i in range(1,51):
    print(i,"\t",end="")
    
for i in range(10,51):
    if i%5==0:
        print(i)

for i in range(1,100):
    if i%2==0:
        print(i,"\t",i**2)
        
sayı=int(input("bir sayı giriniz: "))
faktoriyel=1
for i in range(sayı,1,-1):
    faktoriyel*=i
print(faktoriyel)

for i in range(1,11):
    for j in range(1,6):
     print("i:",i,"*j",j,"=",i*j,"\t",end="")
    print("\n",end="")
toplam=0
liste=[]
liste.append(1)
liste.append(1)


for i in range(1,9):
   liste.append(liste[i-1]+liste[i])   
print(liste)
p=[]

n=[]
x=2
while x!=0:
    x=int(input("SAYI: "))
    if x>0:
        p.append(x)
        
    elif x<0:
        n.append(x)

        
print(p)
print(n)

x=0
while x<=50:
    print(x)
    x+=1

x=1
while x!=0:
    x=int(input("sayı: "))
    for i in range(1,x+1):
        
        for j in range(i):
            print("*",end="")
        print()
    for i in range(x-1,0,-1):
        
        for j in range(i):
            print("*",end="")
        print()


liste=list()
liste=[]
for i in range(0,71):
   if i%5==0:
       liste.append(i)
liste.remove(45)
liste.insert(6,"istanbul")
print(liste)
sayı=len(liste)
print(sayı)

sozluk={"bir":1,"iki":2,"üç":3,"dört":4}
print(sozluk["dört"])

sözlük={"engineer":"mühendis","teacher":"öğretmen","lawyer":"avukat","mechanic":"tamirci"}
print(sözlük.get("teacher"))

sözlük["love"]="sevmek"
print(sözlük)


hesap={"user":123,"passport":"pass","student":"st"}
hesap["user"]=123456
hesap.pop("student")
hesap["admin"]="adm"

print(hesap.get("user"))


mevsimler={"yaz":["haziran","temmuz","ağustos"]}

sözlük={"sayı":(1,2,3)}
print(sözlük)

satır=int(input("satır sayısınız giriniz:"))
sayac=satır-1
for i in range(0,satır,1):
    print(" "*sayac,end="")
    sayac-=1
    for j in range(0,i*2+1):
        print("*",end="")
    print(" ")
    
sayı=int(input("bir sayı giriniz:"))
print("*"*sayı)  
for i in range(1,sayı-2):
    print("*"," "*(sayı-4),"*\t")
print("*"*sayı)

sayı=int(input("sayı giriniz:"))
for i in range(0,sayı+1):
    
    print(" "*(i-1),"*"*i)
    
def irem(x):
    for i in range(i+1,x):
        print("irem elçi\t")
        
def gozde(x):
    
    for i in range(x+1):
        print("gözde")
    

    
sayı=int(input("bir sayı giriniz: "))  
gozde(sayı)

def sayıi(x,y):
    if(x>y):
       for i in range(x,y-1,-1):
            print(i)
    else:
        for i in range(x,y+1):
            print(i)
         
        



sayı=int(input("bir sayı giriniz:"))
sayı2=int(input("bir sayı giriniz:"))
sayıi(sayı,sayı2)


kelime=input("kelimeyi giriniz:")
if len(kelime)%2==0:
    print(kelime.upper())
else:
    print(kelime[0:len(kelime):2])

 
def çarpan():
     sayı=int(input("bir sayı giriniz: "))
     for i in range(1,sayı+1):
         if(sayı%i==0):
             print("çarpan: ",i)
     
çarpan() """                                                                                                                                                                                                                                                                                                                                                                                                
def asalçarpan():
     sayı=int(input("bir sayı giriniz: "))
     for i in range(2,int((sayı/2)+1)):
         asal=True
         if(sayı%i==0):
             for j in range(2,i+1):
                 asal=False
        
             print("asal çarpan: ",i)
     

asalçarpan()













        
    








    
