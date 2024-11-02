# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:56:48 2024

@author: ABDULLAH
"""
bakiye=1000.0
while True:
    işlem=input("Bir işlem seçiniz:  (1.Para Çekme 2.Para Yatırma 3.Bakiye Sorgulama 4.Çıkış ,Seçilen İşlen numarası: ")
    if işlem=="1"or işlem=="2" or işlem=="3"or işlem=="4":
        çekilen=0.0
        yatırılan=0.0
        if işlem=="1" :
            çekilen=float(input("Çekmek istediğiniz tutarı giriniz: "))
            if bakiye <= çekilen :
                print("Mevcut Bakiyeden fazlasını çekemezsiniz")
                continue
            elif  çekilen<=0:
                print("Sıfırdan büyük bir tutar giriniz.")
                continue
            else:
                bakiye-=çekilen
            print("Bakiye: ",bakiye,"TL")
            continue
        elif işlem=="2":
            yatırılan=float(input("Yatırmak istediğiniz tutarı giriniz: "))
            if  yatırılan<=0:
                print("Sıfırdan büyük bir tutar giriniz.")
                continue            
            else:
                bakiye+=yatırılan
                print("Bakiye: ",bakiye,"TL")
                continue
        elif işlem=="3":
            print("Bakiye: ",bakiye,"TL")
            continue
        elif işlem=="4"  :
            print("Çıkış Yaptınız")
        break
    else:
        print("Hatalı Seçim Yaptınız.Lütfen 1-2-3-4 numaralı seçeneklerden birisini seçiniz.")
        
        