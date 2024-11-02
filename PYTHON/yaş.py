# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:40:07 2024

@author: ABDULLAH
"""
import datetime
from datetime import date
gün=int(input("Doğum gününüzü giriniz: "))
ay=int(input("Doğum ayınızı giriniz: "))
yıl=int(input("Doğum yılınızı giriniz: "))
bugün=datetime.date.today()
print("Bugünün tarihi:",bugün)
doğumtarihi=date(yıl,ay,gün)
print("Doğum tarihi:",doğumtarihi)
fark=bugün-doğumtarihi
print(f"{fark.days // 365} yıl, {(fark.days % 365) // 30} ay, {(fark.days % 365) % 30} gün")




