# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:28:35 2024

@author: ABDULLAH
"""

import streamlit as st
import datetime
import sqlite3


conn=sqlite3.connect('hayvanat_bahcesi.db')
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS hayvan
               (id INTEGER PRIMARY KEY ,adı TEXT,tur TEXT,secilipersonel TEXT,yem TEXT,cinsiyet TEXT,
                saglık TEXT,durum TEXT,yas INTEGER,ogun TEXT,ogun_yemek TEXT,
                dogum DATE,gelis_tarih DATE)
               ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS personel
               (id INTEGER PRIMARY KEY ,adı TEXT,soyadi TEXT,adres TEXT,baktiklari TEXT,cinsiyet TEX,
                alan TEXT,durum TEXT,yas INTEGER,telefon INTEGER,maas INTEGER,giris_tarih DATE)
               ''')
conn.commit()
def format_date(date_str):
    if isinstance(date_str, str):
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    return date_str

def format_time(time_str):
    if isinstance(time_str, str):
        return datetime.datetime.strptime(time_str, "%H:%M:%S").time()
    return time_str
def yemek_sifirlama():
    gecerlizaman = datetime.datetime.now().time()

    if gecerlizaman.hour == 0 and gecerlizaman.minute == 0:
        
        cursor.execute("UPDATE hayvan SET ogun_yemek = 0")
        conn.commit()
        st.success("Yemek verileri sıfırlandı.")

def hayvan_yemek_durumu(hayvan_id):
    gecerlizaman = datetime.datetime.now().time()
    
    if 6 <= gecerlizaman.hour < 12:
        ogun = "Sabah"
        ogun_yemek = "sabah_yemek_saati"
    elif 12 <= gecerlizaman.hour < 18:
        ogun = "Öğle"
        ogun_yemek = "ogle_yemek_saati"
    elif 18 <= gecerlizaman.hour < 24:
        ogun = "Akşam"
        ogun_yemek = "aksam_yemek_saati"
    else:
        ogun = None
        ogun_yemek = None

    if ogun:
        st.subheader(f"{ogun} Yemek Durumu")

        cursor.execute(f"SELECT {ogun_yemek} FROM hayvan WHERE id = ?", (hayvan_id,))
        beslenme = cursor.fetchone()

        if beslenme:
            durum = "Yemek Yedildi" if beslenme[0] else "Yemek Yemedi"
            st.write(durum)

            if st.button(f"{ogun} Yedimi?", key=f"{ogun}_yemek_{hayvan_id}"):
                yeni_durum = 1 if beslenme[0] == 0 else 0
                cursor.execute(f"UPDATE hayvan SET {ogun_yemek} = ? WHERE id = ?", (yeni_durum, hayvan_id))
                conn.commit()
                st.success(f"{ogun} yemeği durumu güncellendi.")
        else:
            st.write("Veri yok.")
    else:
        st.warning("Geçerli bir yemek zamanı bulunamadı.")
def hayvan_ekle():
    
    st.title("Hayvan Ekle")
    hayvan_gelis_tarih = st.date_input("Geliş Tarihi")
    hayvan_adı=st.text_input("Hayvan Adı")
    hayvan_tur=st.text_input("Hayvan Türü")
    
    cursor.execute("SELECT id, adı, soyadi FROM personel")
    personeller = cursor.fetchall()
    hayvan_personel = st.multiselect("Bakıcı Seçin", [f"{personel[1]} {personel[2]}" for personel in personeller])
    hayvan_yem=st.text_input("Yem Adı")
    hayvan_cinsiyet= st.selectbox("Cinsiyet", ["Erkek", "Dişi"])
    hayvan_saglık=st.selectbox("Sağlık Durumu", ["Sağlıklı", "Hasta", "Yaralı", "Tedaviye Başlandı", "Tedavisi Devam ediyor"
                                , "Tedavisi Bitti", "Ameliyat olucak ", "Ameliyat Oldu", "Sakat", "Yemek Yemiyor"])
    hayvan_durum=st.text_input("Açıklama")
    hayvan_yas=st.slider("Yaş",1,100)
    hayvan_dogum = st.date_input("Doğum Tarihi")
    ogun = st.selectbox("Öğün Adı", ["Sabah", "Öğle", "Akşam"]) 
    ogun_yemek = st.time_input("Yemek Saati")
    submit=st.button("Kaydet")
    if submit:
        secili_personel_ids = [
            personel[0] for personel in personeller if f"{personel[1]} (ID: {personel[0]})" in hayvan_personel]
        secilipersonel = ",".join(map(str, secili_personel_ids)) if secili_personel_ids else None
        ogun_yemek = ogun_yemek.strftime("%H:%M:%S")
        cursor.execute('''INSERT INTO hayvan (adı, tur, secilipersonel, yem, cinsiyet, saglık, durum, yas,
                                            ogun ,ogun_yemek, dogum, gelis_tarih)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (hayvan_adı, hayvan_tur, secilipersonel, hayvan_yem, hayvan_cinsiyet,hayvan_saglık, hayvan_durum,
         hayvan_yas,ogun ,ogun_yemek, hayvan_dogum, hayvan_gelis_tarih))
        conn.commit()
        st.success("kaydedildi.")
        
def hayvan_listele():
    
    st.title("Kayıtlı Hayvanlar")
    cursor.execute('SELECT id,adı,tur  FROM hayvan' )
    hayvanlar = cursor.fetchall()
    for hayvan in hayvanlar:
        st.write(f"No: {hayvan[0]}, Adı: {hayvan[1]}, Tür: {hayvan[2]}")

def hayvan_bilgileri_goster():
    
    st.title("Hayvan Bilgilerini Göster")
    cursor.execute("SELECT id, adı, tur FROM hayvan")
    hayvanlar = cursor.fetchall()
    
    if not hayvanlar:
        st.warning("Gösterilecek hayvan yok.")
        return
    
    hayvan_secimi = st.selectbox(
        "Hayvan Seçimi",
        [f"{hayvan[1]} ({hayvan[2]})" for hayvan in hayvanlar])
    secili_hayvan_id = hayvanlar[
        [f"{hayvan[1]} ({hayvan[2]})" for hayvan in hayvanlar].index(hayvan_secimi)][0]
    
    
    cursor.execute("SELECT * FROM hayvan WHERE id = ?", (secili_hayvan_id,))
    secili_hayvan = cursor.fetchone()
    
    if "secili_hayvan_goster" not in st.session_state:
        st.session_state["secili_hayvan_goster"] = False  
    
    
    if st.button("Göster/Gizle", key="goster_hayvan"):
        st.session_state["secili_hayvan_goster"] = not st.session_state["secili_hayvan_goster"]  

    if st.session_state["secili_hayvan_goster"]:
        st.subheader("Hayvan Detayları")
        st.write(f"- **Geliş Tarihi**: {secili_hayvan[12]}")
        st.write(f"- **Adı ve Türü**: {secili_hayvan[1]} {secili_hayvan[2]}")
        st.write(f"- **Bakıcı**: {secili_hayvan[3]}")
        st.write(f"- **Yem**: {secili_hayvan[4]}")
        st.write(f"- **Cinsiyet**: {secili_hayvan[5]}")
        st.write(f"- **Sağlık**: {secili_hayvan[6]}")
        st.write(f"- **Durum**: {secili_hayvan[7]}")
        st.write(f"- **Yaş**: {secili_hayvan[8]}")
        st.write(f"- **Öğün Yemek **: {secili_hayvan[9]}")
        st.write(f"- ** Yemek Saati**: {secili_hayvan[10]}")
     
        st.write(f"- **Doğum Tarihi**: {secili_hayvan[11]}")
    
    if st.button("Güncelle", key="guncelle_hayvan"):
        st.session_state["secili_hayvan_guncelle"] = True

    if "secili_hayvan_guncelle" in st.session_state and st.session_state["secili_hayvan_guncelle"]:
        st.subheader(f"Hayvan Bilgilerini Güncelle: {secili_hayvan[1]} ({secili_hayvan[2]})")
        cursor.execute("SELECT id, adı, tur FROM hayvan")
        hayvanlar = cursor.fetchall()
        
        if not hayvanlar:
            st.warning("Güncellenecek hayvan yok.")
            return
        hayvan_dogum_degeri_1 = secili_hayvan[11]

        if isinstance(hayvan_dogum_degeri_1, str):  
            hayvan_dogum_degeri = datetime.datetime.strptime(hayvan_dogum_degeri_1, "%Y-%m-%d").date()
        else:  
            hayvan_dogum_degeri = hayvan_dogum_degeri_1
        
        hayvan_gelis_tarih_1 = secili_hayvan[12]
        
        if isinstance(hayvan_gelis_tarih_1, str):  
            hayvan_gelis_tarih = datetime.datetime.strptime(hayvan_gelis_tarih_1, "%Y-%m-%d").date()
        else:  
            hayvan_gelis_tarih = hayvan_gelis_tarih_1
       
        hayvan_gelis_tarih = st.date_input("Geliş Tarihi", value=hayvan_gelis_tarih)
        hayvan_dogum = st.date_input("Doğum Tarihi", value=hayvan_dogum_degeri)
        hayvan_adı = st.text_input("Adı", secili_hayvan[1])
        hayvan_tur = st.text_input("Tür", secili_hayvan[2])
        cursor.execute("SELECT id, adı, soyadi FROM personel")
        personeller = cursor.fetchall()
        hayvan_personel = st.multiselect("Bakıcı Seçin",[f"{personel[1]} {personel[2]}"for personel in personeller],secili_hayvan[3])
        hayvan_yem = st.text_input("Yem Adı", secili_hayvan[4])
        hayvan_cinsiyet = st.selectbox("Cinsiyet", ["Erkek", "Dişi"], index=["Erkek", "Dişi"].index(secili_hayvan[5]))
        saglık_durumlari = ["Sağlıklı", "Hasta", "Yaralı", "Tedaviye Başlandı", "Tedavisi Devam ediyor",
                        "Tedavisi Bitti", "Ameliyat olucak ", "Ameliyat Oldu", "Sakat", "Yemek Yemiyor"]
        hayvan_saglık = st.selectbox("Sağlık", saglık_durumlari,saglık_durumlari.index(secili_hayvan[6]))
        hayvan_durum = st.text_input("Durum", secili_hayvan[7])
        hayvan_yas = st.slider("Yaş", 1, 100, secili_hayvan[8])
        ogunlar = ["Sabah", "Öğle", "Akşam"]
        ogun_index = ogunlar.index(secili_hayvan[9]) if secili_hayvan[9] in ogunlar else 0
        ogun = st.selectbox("Öğün Adı", ogunlar, index=ogun_index)
        try:
            ogun_yemek = datetime.datetime.strptime(secili_hayvan[10], "%H:%M:%S").time()
        except ValueError:
            ogun_yemek = datetime.time(0, 0)  
        ogun_yemek = st.time_input("Yemek Saati", value=ogun_yemek)  
        ogun_yemek = ogun_yemek.strftime("%H:%M:%S")
        if  st.button("Kaydet", key="kaydet_hayvan"):
            

            hayvan_personel = ",".join(hayvan_personel) if hayvan_personel else None
            cursor.execute('''
                UPDATE hayvan
                SET adı = ?, tur = ?, secilipersonel = ?, yem = ?, cinsiyet = ?, saglık = ?, durum = ?, yas = ?,
                ogun = ?,ogun_yemek = ? ,dogum = ?, gelis_tarih = ?
                WHERE id = ?''',
                (hayvan_adı, hayvan_tur, hayvan_personel,hayvan_yem,hayvan_cinsiyet,hayvan_saglık,hayvan_durum,hayvan_yas,
                 ogun ,ogun_yemek , hayvan_dogum, hayvan_gelis_tarih,
                 secili_hayvan_id))
            conn.commit()
            st.success("Bilgiler güncellendi.")
            st.session_state["secili_hayvan_guncelle"] = False
    
    if st.button("Sil"):
            cursor.execute('DELETE FROM hayvan WHERE id = ?', (secili_hayvan[0],))
            conn.commit()
            st.success(f"{secili_hayvan[1]} adlı hayvan başarıyla silindi.")


def personel_ekle():
    
    st.title("Personel Ekle")
    personel_adı=st.text_input("Personel Adı")
    personel_soyadi=st.text_input("Personel Soyadı")
    personel_giris_tarih=st.date_input("İşe Giriş Tarihi")
    personel_adres=st.text_input("Personel Adresi")  
    cursor.execute('SELECT id,adı,tur  FROM hayvan' )
    hayvanlar = cursor.fetchall()
    secili_hayvanlar = st.multiselect(
    "Hayvanları Seçin",[f"{hayvan[1]} {hayvan[2]}" for hayvan in hayvanlar])
    personel_cinsiyet = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
    personel_alan=st.text_input("Personel Alanı")
    personel_durum = st.selectbox("Personel Durumu", 
                            ["Yönetici", "Bakıcı", "Temizlik", "Güvenlik", "Veteriner", "Ahçı"])
    personel_yas=st.slider("Yaş",18,60)
    personel_telefon = st.text_input("Telefon")
    personel_maas = st.number_input("Maaş")
    submit=st.button("Kaydet")
    
    if submit:
        secili_hayvan_ids = [
            hayvan[0] for hayvan in hayvanlar if f"{hayvan[1]} (ID: {hayvan[0]})" in secili_hayvanlar]
        baktiklari = ",".join(map(str, secili_hayvan_ids)) if secili_hayvan_ids else None
        cursor.execute('''
            INSERT INTO personel (adı, soyadi, adres, baktiklari, cinsiyet, alan, durum, yas, telefon, maas, giris_tarih)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (personel_adı, personel_soyadi, personel_adres, baktiklari, 
              personel_cinsiyet, personel_alan, personel_durum, personel_yas, 
              personel_telefon, personel_maas, personel_giris_tarih))
        conn.commit()
        st.success("kaydedildi.")
        
def personel_listele():
    
    st.title("Kayıtlı Personeller")
    cursor.execute("SELECT id, adı, soyadi,durum FROM personel")
    personeller = cursor.fetchall()
    for personel in personeller:
        st.write(f"No: {personel[0]}, Adı: {personel[1]}, Soyadı: {personel[2]}, Durum: {personel[3]}")
        
def personel_bilgileri_goster():
    
    st.title("Personel Bilgilerini Göster")
    cursor.execute('SELECT * FROM personel')
    personeller = cursor.fetchall()
    
    if not personeller:
        st.warning("Henüz kayıtlı bir personel yok!")
        return

    personel_secimi = st.selectbox(
        "Personel Seçimi",
        [f"{personel[1]} {personel[2]}" for personel in personeller],
        key="personel_secimi")
    secili_personel_id = personeller[
        [f"{personel[1]} {personel[2]}" for personel in personeller].index(personel_secimi)][0]
    cursor.execute("SELECT * FROM personel WHERE id = ?", (secili_personel_id,))
    secili_personel = cursor.fetchone()
    
    if "secili_personel_goster" not in st.session_state:
        st.session_state["secili_personel_goster"] = False  
        
    if st.button("Göster/Gizle", key="goster_personel"):
        st.session_state["secili_personel_goster"] = not st.session_state["secili_personel_goster"]  
        
    if st.session_state["secili_personel_goster"]: 
        st.subheader("Personel Detayları")
        st.write(f"- **İşe Giriş Tarihi**: {secili_personel[11]}")
        st.write(f"- **Adı ve Soyadı**: {secili_personel[1]} {secili_personel[2]}")
        st.write(f"- **Adres**: {secili_personel[3]}")
        st.write(f"- **Baktığı Hayvanlar**: {secili_personel[4]}")
        st.write(f"- **Cinsiyet**: {secili_personel[5]}")
        st.write(f"- **Alan**: {secili_personel[6]}")
        st.write(f"- **Durum**: {secili_personel[7]}")
        st.write(f"- **Yaş**: {secili_personel[8]}")
        st.write(f"- **Telefon**: {secili_personel[9]}")
        st.write(f"- **Maaş**: {secili_personel[10]}")
        
    if st.button("Güncelle", key="guncelle_personel"):
        st.session_state["secili_personel_guncelle"] = True
        
    if "secili_personel_guncelle" in st.session_state and st.session_state["secili_personel_guncelle"]:
        st.subheader(f"Personel Bilgilerini Güncelle: {secili_personel[1]} ({secili_personel[2]})")
        cursor.execute("SELECT id, adı, soyadi,durum FROM personel")
        personeller = cursor.fetchall()
        if not personeller:
            st.warning("Güncellenecek personel yok.")
            return
        
        personel_giris_tarih_1 = secili_personel[11]
        if isinstance(personel_giris_tarih_1, str):
            personel_giris_tarih = datetime.datetime.strptime(personel_giris_tarih_1, "%Y-%m-%d").date()
        else:
            personel_giris_tarih = personel_giris_tarih_1
            
        personel_adı=st.text_input("Personel Adı", secili_personel[1])
        personel_soyadi=st.text_input("Personel Soyadı", secili_personel[2])
        personel_giris_tarih = st.date_input("İşe Giriş Tarihi", value=personel_giris_tarih)
        personel_adres=st.text_input("Personel Adresi", secili_personel[3])
        cursor.execute("SELECT id, adı, tur FROM hayvan")
        hayvanlar = cursor.fetchall()
        hayvanlar_options = [f"{hayvan[1]} {hayvan[2]}" for hayvan in hayvanlar]
        
        if secili_personel[4]:
            personel_baktiklari_default = secili_personel[4].split(",")
        else:
            personel_baktiklari_default = []
        personel_baktiklari = st.multiselect(
            "Baktığı Hayvanlar", 
            hayvanlar_options, 
            default=[item for item in personel_baktiklari_default if item in hayvanlar_options])
        personel_cinsiyet = st.selectbox("Cinsiyet", ["Erkek", "Dişi"], index=["Erkek", "Dişi"].index(secili_personel[5]))
        personel_alan=st.text_input("Personel Alanı", secili_personel[6])
        personel_durum = st.selectbox("Personel Durumu", 
                                ["Yönetici", "Bakıcı", "Temizlik", "Güvenlik", "Veteriner", "Ahçı"],
                                index=["Yönetici", "Bakıcı", "Temizlik", "Güvenlik", "Veteriner", "Ahçı"].index(secili_personel[7]))

        personel_yas=st.slider("Yaş",18,60, secili_personel[8])
        personel_telefon = st.text_input("Telefon", secili_personel[9])
        personel_maas = st.number_input("Maaş", secili_personel[10])
        
        if st.button("Kaydet", key="kaydet_personel"):
            personel_baktiklari = ",".join(personel_baktiklari) if personel_baktiklari else None
            cursor.execute('''
                UPDATE personel
                SET adı = ?, soyadi = ?, adres = ?, baktiklari = ?, cinsiyet = ?, alan = ?, durum = ?,
                yas = ?, telefon = ?, maas = ?, giris_tarih = ?
                WHERE id = ?
            ''', (personel_adı, personel_soyadi, personel_adres, personel_baktiklari, personel_cinsiyet, personel_alan, 
                  personel_durum, personel_yas, personel_telefon, personel_maas, personel_giris_tarih, secili_personel_id))

            conn.commit()
            st.success("Bilgiler güncellendi.")
            st.session_state["secili_personel_guncelle"] = False
            
    if st.button("Sil"):
            cursor.execute('DELETE FROM personel WHERE id = ?', (secili_personel[0],))
            conn.commit()
            st.success(f"{secili_personel[1]} adlı personel başarıyla silindi.")
yemek_sifirlama()           

st.sidebar.title("Menü")
selection = st.sidebar.radio("Seçim Yapın", ["Anasayfa", "Hayvan Ekle", "Hayvan Listesi", "Personel Ekle", "Personel Listesi"])
st.title("Hayvanat Bahçesi Uygulaması")
if selection == "Anasayfa":
    st.subheader("Hayvanat Bahçesi Uygulamasına Hoş Geldiniz!")
elif selection == "Hayvan Ekle":
    hayvan_ekle()
elif selection == "Hayvan Listesi":
    hayvan_bilgileri_goster()
    hayvan_listele()
elif selection == "Personel Ekle":
    personel_ekle()
elif selection == "Personel Listesi":
    personel_bilgileri_goster()
    personel_listele()
    
else :
    st.subheader("Anasayfadasınız")



    