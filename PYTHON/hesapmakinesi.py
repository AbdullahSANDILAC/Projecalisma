# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:44:58 2024

@author: ABDULLAH
"""



while(True):
    sayi1=int(input("1.sayıyı giriniz:"))
    sayi2=int(input("2.sayıyı giriniz:"))
    işlem=input("Bir seçenek yazınız:  (toplama/çıkarma/çarpma/bölme/üs alma/mod alma :")
    toplama=sayi1+sayi2
    çıkarma=sayi1-sayi2
    çarpma=sayi1*sayi2
    
    üsalma=sayi1**sayi2
    
    if işlem =="toplama":
        print("sonuc:",toplama)
    elif işlem =="çıkarma":
        print("sonuc:",çıkarma)
    elif işlem =="çarpma":
        print("sonuc:",çarpma)
    elif işlem == "bölme" and sayi2==0:
            print("2.sayı Sıfırdan farklı bir sayıolmalıdır")
    elif işlem == "bölme" and sayi2 != 0:
        bölme=sayi1/sayi2
        print("sonuc:",bölme)
    elif işlem =="üs alma":
        print("sonuc:",üsalma)
    elif işlem =="mod alma":
        if sayi2!=0  :
            modalma=sayi1%sayi2
            print("sonuc:",modalma)
        
            continue
        else:
            print("2.sayı Sıfırdan farklı bir sayıolmalıdır")

    else:
        print("Geçersiz seçenek. Lütfen 'toplama', 'çıkarma', 'çarpma', 'bölme', 'üs alma', 'mod alma' yazın.")
        continue
    