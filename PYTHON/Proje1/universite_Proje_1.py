# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:54:48 2024

@author: ABDULLAH
"""

import streamlit as st
import requests
import json


st.title("Üniversiteler")
getir=st.button("Üniversite getir")
kaydet=st.button("Üniversite Kaydet")
listele=st.button("Üniversite Listele")


name = st.text_input("Üniversite Adı")
web_pages = st.text_input("Web Sayfası")
ekle=st.button("Üniversite Ekle")


def universite_kaydet():
    url="http://universities.hipolabs.com/search?country=Turkey"
    cevap=requests.get(url)
    if cevap.status_code==200:
        data=cevap.json()
        with open("universite.json","w",encoding="utf-8") as file:
            json.dump(data,file)
        st.success("Üniversite Bilgileri Dosyaya Kaydedildi.")
        
def universite_getir():
    url="http://universities.hipolabs.com/search?country=Turkey"
    cevap=requests.get(url)
    if cevap.status_code==200:
        data=cevap.json()
        st.write("Getirilen  Üniversiteler")
        for universite in data:
            st.write(f"**{universite['name']}** ------ {universite['web_pages']}")
    else:
        print("siteye bağlanamadı")
        st.write("-----")
    
def universite_ekle():       
    with open("universite.json","r",encoding="utf-8")as file:
        data=json.load(file)
        #yeni_id=len(data["universite"])+1
        yeni_üniversite={
            #"id":yeni_id,
            "name":name,
            "web_pages":web_pages
            }
    data["universite"].append(yeni_üniversite)
    with open("universite.json","w",encoding="utf-8")as file:
        json.dump(data,file)
    st.success("Üniversite '{name} Dosyaya Eklendi.")

def universite_listele ():
    with open("universite.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    if data:
        st.write("Üniversiteler")
        for universite in data:
            st.write(f"{universite['name']},**({universite['web_pages'][0]})")

if listele:
    universite_listele()

if getir:
    universite_getir()
        
if kaydet:
    universite_kaydet()

if ekle:
    universite_ekle(name,web_pages)
   








