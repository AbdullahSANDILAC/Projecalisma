# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:53:11 2024

@author: ABDULLAH
"""
faiz=0.0
kredi=0.0
süre=0.0

while True:
    kreditürü=input("Kredi türü seçiniz:  (ihtiyaç/taşıt/konut ,Seçilen kredi türü: ")
    if kreditürü=="ihtiyaç"or kreditürü=="taşıt" or kreditürü=="konut":
        kredi=float(input("Çekmek istediğiniz tutarı giriniz: "))
        süre=int(input("Kredi süresini aylık olarak giriniz: "))
        if  kredi<=0 or süre<=0:
            print("Sıfırdan büyük bir değer giriniz.")
            continue
        if kreditürü=="ihtiyaç" :
                faiz=1.5
        elif kreditürü=="taşıt":
                faiz=1.2
        elif kreditürü=="konut":
                faiz=1.0
        Toplamödeme=kredi*(1+faiz/100*süre)
        
        print("Konut kredisi Toplam Geri Ödeme: ",Toplamödeme,"TL")
            
       
        break
    else:
        print("Hatalı Seçim Yaptınız.Lütfen kredi türlerinden birisini seçiniz.")
        
       
        