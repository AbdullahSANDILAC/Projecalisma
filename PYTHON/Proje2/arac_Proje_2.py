# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:39:55 2024

@author: ABDULLAH
"""
import streamlit as st
from datetime import date
import json

st.title("Araç Kiralama ")
st.sidebar.header("Kiralama Bilgilerini Giriniz")

class Arac:
    def __init__(self,marka,model,vites_tipi,yil,yakit_turu,yas,resim,fiyat):
        self.marka=marka
        self.model=model
        self.vites_tipi=vites_tipi
        self.yil=yil
        self.yakit_turu=yakit_turu
        self.yas=yas
        self.resim=resim
        self.fiyat = fiyat
   
    def bilgileri_goster(secili_arac,gun):
        
        toplam_ucret = gun * secili_arac.fiyat
        st.subheader("Kiralama Detayları")
        st.image(secili_arac.resim, width=300)
        st.write(f"- **Marka ve Model**: {secili_arac.marka} {secili_arac.model}")
        st.write(f"- **Yıl**: {secili_arac.yil}")
        st.write(f"- **Vites Tipi**: {secili_arac.vites_tipi}")
        st.write(f"- **Yakıt Türü**: {secili_arac.yakit_turu}")
        st.write(f"- **Günlük Ücret**: {secili_arac.fiyat} TL")
        st.write(f"- **Minimum Yaşınız**: {secili_arac.yas} TL")
        st.write(f"- **Toplam Kiralama Süresi**: {gun} gün")
        st.write(f"- **Toplam Kiralama Ücreti**: {toplam_ucret} TL")
        
def kullanici_goster(isim=None, mail=None):
    
        with open("yorum.txt", "r", encoding="utf-8") as file:
            data = json.load(file)
        if isim and mail:
            for kullanici in data["kullanicilar"]:
                if kullanici["isim"] == isim and kullanici["mail"] == mail:
                    return kullanici
            return None

        for kullanici in data["kullanicilar"]:
            st.write(f" **  {kullanici['isim']}**")
            st.write(f"     {kullanici['yorum']}")

def yorum_guncelle(isim, mail, yeni_yorum):
    with open("yorum.txt","r",encoding="utf-8")as file:
        data=json.load(file)
        for kullanici in data["kullanicilar"]:
            if kullanici["isim"] == isim and kullanici["mail"] == mail:
                kullanici["yorum"] = yeni_yorum  
                with open("yorum.txt", "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False)
                return True
        return False
        
def kullanici_ekle(isim,mail,yorum):
    with open("yorum.txt","r",encoding="utf-8")as file:
        data=json.load(file)
    yeni_kullanici={
        "isim":isim,
        "mail":mail,
        "yorum":yorum
                    }
    data["kullanicilar"].append(yeni_kullanici)
    with open("yorum.txt","w",encoding="utf-8")as file:
        json.dump(data,file)

araba1=Arac("Fiat","Egea","Manuel",2020,"Benzin","21","https://www.avis.com.tr/Avis/media/Avis/Cars/f-renault-clio-at.png",1250)
araba2=Arac("Fiat","Egea Cross","Manuel",2021,"Dizel","21","https://www.avis.com.tr/Avis/media/Avis/Cars/a-fiat-egea.png",1500)
araba3=Arac("Ford ","Odak","Manuel",2022,"benzin","21","https://www.avis.com.tr/Avis/media/Avis/Cars/o-ford-focus.png",1500)
araba4=Arac("Ford ","Puma","Manuel",2022,"benzin","21","https://www.avis.com.tr/Avis/media/Avis/Cars/p-ford-puma.png",1750)
araba5=Arac("Ford ","Kuga","Manuel",2022,"benzin","21","https://www.avis.com.tr/Avis/media/Avis/Cars/d-ford-kuga.png",1750)
araba6=Arac("BMW ","IX1","Manuel",2022,"benzin","23","https://www.avis.com.tr/Avis/media/Avis/Cars/g-bmw-ix1.png",2000)
araba7=Arac("BMW","2 Serisi","Manuel",2023,"benzin","23","https://www.avis.com.tr/Avis/media/Avis/Cars/h-bmw-2-serisi.png",2000)
araba8=Arac("Volkswagen ","Passat Varyantı","Manuel",2023,"benzin","23","https://www.avis.com.tr/Avis/media/Avis/Cars/j-volkswagen-passat-variant.png",2000)
araba9=Arac("Volvo ","XC40","Manuel",2023,"benzin","23","https://www.avis.com.tr/Avis/media/Avis/Cars/m-volvo-xc40.png",2250)
araba10=Arac("Fiat","Egea","Otomatik",2020,"Benzin","21","https://www.avis.com.tr/Avis/media/Avis/Cars/f-renault-clio-at.png",1500)
araba11=Arac("Fiat","Egea Cross","Otomatik",2021,"Dizel","21","https://www.avis.com.tr/Avis/media/Avis/Cars/a-fiat-egea.png",1750)
araba12=Arac("Ford ","Odak","Otomatik",2022,"benzin","21","https://www.avis.com.tr/Avis/media/Avis/Cars/o-ford-focus.png",1750)
araba13=Arac("Ford ","Puma","Otomatik",2022,"benzin","21","https://www.avis.com.tr/Avis/media/Avis/Cars/p-ford-puma.png",2000)
araba14=Arac("Ford ","Kuga","Otomatik",2022,"benzin","21","https://www.avis.com.tr/Avis/media/Avis/Cars/d-ford-kuga.png",2000)
araba15=Arac("BMW ","IX1","Otomatik",2022,"benzin","23","https://www.avis.com.tr/Avis/media/Avis/Cars/g-bmw-ix1.png",2000)
araba16=Arac("BMW","2 Serisi","Otomatik",2023,"benzin","23","https://www.avis.com.tr/Avis/media/Avis/Cars/h-bmw-2-serisi.png",2250)
araba17=Arac("Volkswagen ","Passat Varyantı","Otomatik",2023,"benzin","23","https://www.avis.com.tr/Avis/media/Avis/Cars/j-volkswagen-passat-variant.png",2250)
araba18=Arac("Volvo ","XC40","Otomatik",2023,"benzin","23","https://www.avis.com.tr/Avis/media/Avis/Cars/m-volvo-xc40.png",2250)


araclar = {
    "Seçiniz":[araba1, araba2, araba3, araba4, araba5, araba6, araba7, araba8, araba9,araba10, araba11, araba12, araba13, araba14, araba15, araba16, araba17, araba18],
    "Manuel": [araba1, araba2, araba3, araba4, araba5, araba6, araba7, araba8, araba9],
    "Otomatik": [araba10, araba11, araba12, araba13, araba14, araba15, araba16, araba17, araba18]
    }

alis_tarihi = st.sidebar.date_input("Araç Alış Tarihi", min_value=date.today())
teslim_tarihi = st.sidebar.date_input("Araç Teslim Tarihi", min_value=alis_tarihi)
gun=(teslim_tarihi-alis_tarihi).days + 1
vites_tipi = st.sidebar.radio("Vites Tipi", ["Seçiniz","Manuel","Otomatik"])
col1, col2 = st.columns([1, 1])
with col1:
    if gun>0:
        if  vites_tipi=="Seçiniz":
            st.subheader("Mevcut Araçlar")
            for arac in araclar["Seçiniz"]:
                st.image(arac.resim, width=300)
                st.write(f"- **Marka ve Model**: {arac.marka} {arac.model}")
                st.write(f"- **Yıl**: {arac.yil}")
                st.write(f"- **Vites Tipi**: {arac.vites_tipi}")
                st.write(f"- **Yakıt Türü**: {arac.yakit_turu}")
                st.write(f"- **Günlük Ücret**: {arac.fiyat} TL")
                st.write(f"- **Minimum Yaşınız**: {arac.yas} TL")
        
        else:
            secili_araclar = araclar[vites_tipi]
            arac_secimi = st.sidebar.radio(
                "Araç Seçimi",
                [f"{arac.marka} {arac.model} ({arac.yil}) - {arac.fiyat} TL/gün" for arac in secili_araclar]
            )
            secili_arac = secili_araclar[[f"{arac.marka} {arac.model} ({arac.yil}) - {arac.fiyat} TL/gün" for arac in secili_araclar].index(arac_secimi)]
            
            if st.sidebar.button("Kiralama Detayları", key="hesap"):
                secili_arac.bilgileri_goster(gun)
               
            Kiralama=st.sidebar.button("Kiralamak İçin Tıklayınız")
            
            
            if "is_form_submitted" not in st.session_state:
                st.session_state.is_form_submitted = False
          


            if Kiralama and not st.session_state.is_form_submitted:
                with st.form("my_form"):
                    st.header("Formu Doldurunuz")
                    isim = st.text_input("İsminiz:")              
                    mail = st.text_input("E-posta:")
                    kartno = st.text_input("Kart Numaranız:")
                    karttarih = st.text_input("Son kullanım tarihiniz :", placeholder="Kartın Son kullanım tarihi ay/yıl  ",)
                    kod = st.text_input("Güvenlik kodunuz:")
                    yorum = ''
                    st.write(f"- **Alış Tarihi**: {alis_tarihi}")
                    st.write(f"- **Teslim Tarihi**: {teslim_tarihi}")
                    st.write(f"- **Marka ve Model**: {secili_arac.marka} {secili_arac.model}")
                    st.write(f"- **Yıl**: {secili_arac.yil}")
                    st.write(f"- **Vites Tipi**: {secili_arac.vites_tipi}")
                    st.write(f"- **Ödenecek Tutar**: {gun * secili_arac.fiyat} TL")
                    Kirala=st.form_submit_button("İşlemini Tamamla")
                    
                    if Kirala:
                        if isim and mail and yorum and kartno and karttarih and kod:
                            kullanici_ekle(isim,mail,yorum)
                            
                            st.success("Kiralama  işlemi başarılı!")
                            st.session_state.is_form_submitted = True
                        else:
                            st.error("Lütfen tüm alanları doldurunuz.")
                
    if gun<=0:
        st.write("Teslim tarihi Aldığınızdan tarihten önce olamaz.")

with col2:
    st.header("Yorum Ekle")
    isim = st.text_input("İsminiz:", key="isim")
    mail = st.text_input("E-posta:", key="mail")
    yorum = st.text_area("Yorumunuz:", placeholder="Görüşlerinizi paylaşın...", key="yorum")

    if st.button("Yorum Gönder", key="gonder"):
        if isim and mail and yorum:
            mevcut_kullanici = kullanici_goster(isim=isim, mail=mail)
            if mevcut_kullanici:
                yorum_guncelle(isim, mail, yorum)
                st.success("Yorumunuz güncellendi!")
            else:
                kullanici_ekle(isim, mail, yorum)
                st.success("Yorumunuz kaydedildi!")
        else:
            st.error("Lütfen tüm alanları doldurunuz.")
    st.subheader("Yapılan Yorumlar")
    kullanici_goster()
                


            





