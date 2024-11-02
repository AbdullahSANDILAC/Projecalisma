# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 21:06:43 2024

@author: ABDULLAH
"""
ogrenciler = []
ID=1
while True:
    işlem=input("Bir işlem seçiniz:  (1.Öğrenci Ekle 2.Öğrenci Sil 3.Öğrencileri listele 4.Çıkış ,Seçilen İşlen numarası: ")
    if işlem=="1"or işlem=="2" or işlem=="3"or işlem=="4":
        if işlem=="1" :
            ad=input("Öğrenci adını giriniz: ")
            notu=float(input("Öğrenci notunu giriniz: "))
            if notu < 0 :
                print("Not sıfırdan büyük olmalıdır.")
                continue
            elif not ad:
                print("İsminizi  giriniz")
                continue
            
            else:
                ogrenci={"Öğrenci ID":ID,"Öğrenci Adı":ad,"Öğrenci Notu":notu}
                ogrenciler.append(ogrenci)
                print("Öğrenci başarıyla eklendi.")
                print(f"Öğrenci ID: {ID}, Öğrenci Adı: {ad}, Öğrenci Notu: {notu}")
                ID+=1
            continue
        elif işlem=="2":
            sil=int(input("Öğrenci ID'sini giriniz: "))
            for ogrenci in ogrenciler:
                if ogrenci["Öğrenci ID"]==sil:
                   ogrenciler.remove(ogrenci) 
                   print("Öğrenci başarıyla silindi.")
                else:   
                   print("Öğrenci bulunamadı.")
            continue
        elif işlem=="3":
            for ogrenci in ogrenciler:
                print(f"ID: {ogrenci['Öğrenci ID']}, Adı: {ogrenci['Öğrenci Adı']}, Notu: {ogrenci['Öğrenci Notu']}")
            continue
        elif işlem=="4"  :
            print("Çıkış Yaptınız")
        break
    else:
        print("Hatalı Seçim Yaptınız.Lütfen 1-2-3-4 numaralı seçeneklerden birisini seçiniz.")

