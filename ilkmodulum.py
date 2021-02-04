"""
Bu modülde çeşitli hesaplamalar yapılmaktadır.
"""

def toplam(a,b):
    """
    Bu fonksiyon kendisine gönderilen iki değerin toplamını döndürür
    """
    return a+b

def karekok(a):
    """
    Sayının karekökünü geri döndürür
    """
    import math
    s=math.sqrt(a)
    return s

def toplamlarinkaresi():
    a,b=int(input("Sayi 1:")),int(input("Sayi 2:"))
    return toplam(a,b)**2

liste=[4,3,10,6,23,8,46,14,23,6]