# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:47:55 2019

@author: gozdemihranaltinsoy
"""
#%%
class Calisanlar():
    personeller=[]

class Calisan(): 
    #Calisan sınıfı tanımlandı
    unvani="isci"
    maasi=3500
    kabiliyetleri=[]
    print(unvani)


print(Calisan.maasi)
print(Calisan.unvani)

Calisan.maasi=4000
print(Calisan.maasi)

ayse=Calisan()
ayse.maasi=4500
ayse.kabiliyetleri=["raporlama","dakik"]
print(ayse.kabiliyetleri)
print("Çalışan:",Calisan.maasi)
print("Ayşe:",ayse.maasi)

#intance kavramı, ilgili sınıfların bütün özelliklerini taşıyan birer üyesi olması demektir.
#Örnekte ayse Calisan sınıfının özelliklerini taşıyan birer üyesidir. 

ali=Calisan()
mehmet=Calisan()
ali.unvani="Müdür"
#Bu sınıf örneklerini kullanarak, ilgili sınıfın niteliklerine (attribute) erişebiliriz.

Calisan.maasi=2500
print("Ayşe:",ayse.maasi)
print("Calisan:",Calisan.maasi)
print("Ali:",ali.maasi)

class Urun():
    Urunkod=""
    adi=""
    stokadet=0
    
import siparis
cikolata=siparis.Siparis()
cikolata.firma="Marketim"
cikolata.miktar=100
cikolata.siparistarih="1.1.2019"
cikolata.teslimtarih="10.1.2019"
print(cikolata.firma)
print(dir(cikolata))

#%%
class Calisan2():
    def __init__(self):
        self.kabiliyetleri=[]
#Örnek niteliklerini tanımlamak için iki yardımcı araca ihtiyacımız vardır: __init__() fonksiyonu ve self.
        print(self.kabiliyetleri)
#Çünkü self.kabiliyetleri bir sınıf niteliği değil, bir örnek niteliğidir. Örnek niteliklerine erişebilmek için de ilgili sınıfı mutlaka örneklememiz gerekir. Ayrıca sınıf niteliklerinin aksine, örnek niteliklerine sınıf adları üzerinden erişemeyiz. Yani self.kabiliyetleri adlı örnek niteliğine erişmeye yönelik şöyle bir girişim bizi hüsrana uğratacaktır:
#Calisan2.kabiliyetleri
#Bu örnek niteliğine erişmek için örneklendirme mekanizmasından yararlanmamız lazım:
Calisan().kabiliyetleri #parantezlere dikkat!        


ahmet=Calisan2()
#ahmet=Calisan2() kodu yardımıyla, Çalışan sınıfının bir örneğini çıkardık ve buna ahmet adını verdik. İşte tam bu anda __init__() fonksiyonu çalışmaya başladı ve ahmet örneği için, kabiliyetleri adlı boş bir örnek niteliği oluşturdu.

#self kelimesi, Python programlama dilinin söz diziminin gerektirdiği bir öğedir. Bu kelime, Calisan2() adlı sınıfın örneklerini temsil eder. Yani self kelimesi bir sınıfın örneklerini temsil ediyor.

print(ahmet.kabiliyetleri)

class Çalışan():
    personel = ['personel']

    def __init__(self):
        self.kabiliyetleri = []
        
ahmet = Çalışan()
print(ahmet.personel)
#Burada aynı adı taşıyan bir sınıf niteliği ile bir örnek niteliğimiz var. Python’da hem sınıf niteliklerine, hem de örnek niteliklerine örnek isimleri üzerinden erişebileceğiz. Yani eğer örneğimizin ismi ahmet ise, hem kabiliyetleri adlı sınıf niteliğine hem de self.kabiliyetleri adlı örnek niteliğine aynı şekilde erişiyoruz:

ahmet = Çalışan()
print(ahmet.kabiliyetleri)



class Çalışan2():
    kabiliyetleri = ['sınıf niteliği']

    def __init__(self):
        self.kabiliyetleri = ['örnek niteliği']

#sınıf niteliğine erişmek için
#sınıf adını kullanıyoruz
print(Çalışan2.kabiliyetleri)

#örnek niteliğine erişmek için
#örnek adını kullanıyoruz
ahmet = Çalışan2()
print(ahmet.kabiliyetleri)


#%%
class Çalışan():
    def __init__(self):
        self.kabiliyetleri = []
#Yukarıdaki kodları deneme.py adlı bir dosyaya kaydettiğimizi varsayarsak:

import deneme
ahmet = deneme.Çalışan()
ahmet.kabiliyetleri.append('konuşkan')
ahmet.kabiliyetleri

['konuşkan']

mehmet = deneme.Çalışan()
print(mehmet.kabiliyetleri)

