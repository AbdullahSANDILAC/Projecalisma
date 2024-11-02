# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:46:13 2024

@author: ABDULLAH
"""

while(True):
    Hamburgers=input("Hamburger istiyor musunuz? (evet/hayır): ")
    Pizzas=input("Pizza istiyor musunuz:? (evet/hayır): ")
    Salatas=input("Salata istiyor musunuz:? (evet/hayır): ")
    İçeceks=input("İçecek istiyor musunuz:? (evet/hayır): ")
    Tatlıs=input("Tatlı istiyor musunuz:? (evet/hayır): ")
    Hamburger=50.0
    Pizza=75.0
    Salata=30.0
    İçecek=20.0
    Tatlı=25.0
    sepet=0.0
    indirim=0.10
    if Hamburgers=="evet" or Pizzas=="evet" or Salatas=="evet"or İçeceks=="evet"or Tatlıs=="evet" or Hamburgers=="hayır" or Pizzas=="hayır" or Salatas=="hayır"or İçeceks=="hayır"or Tatlıs=="hayır" :
        if Hamburgers=="evet":
            sepet+=Hamburger        
        if Pizzas=="evet":
            sepet+=Pizza
        if Salatas=="evet":
            sepet+=Salata
        if İçeceks=="evet":
            sepet+=İçecek
        if Tatlıs=="evet":
            sepet+=Tatlı
        
    else:
        print("(evet/hayır) seçeneklerinden birisini seçiniz.")
        continue
    print("Sepet Tutarı:",sepet,"TL")
    if sepet>=150:
        tutar=sepet*(1-indirim)
        print("İndirim(150 TL üzeri siparişlerde %10):Uygulandı","İndirim=",sepet*indirim,"TL")
        print("Toplam Tutar:",tutar,"TL")
    else :
         tutar=sepet
         print("İndirim(150 TL üzeri siparişlerde %10):Uygulanmadı")
         print("Toplam Tutar:",tutar,"TL")
         ÖdenenTutar=float(input("Ödediğiniz miktarı giriniz: "))
         paraüstü=ÖdenenTutar-tutar
         print("Para üstü:",paraüstü,"TL")
    break
        
         
     
