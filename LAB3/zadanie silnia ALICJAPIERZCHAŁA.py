# -*- coding: utf-8 -*-
"""
Created on Sat May  8 10:49:14 2021

@author: rawsk
"""

def Nazwafunkcji():
    print("wynik funkcji")
    print("końcowy wynik")
    
def Funkcjaargumentów (zmienna):
    print("podałam zmienną która wynosi = ", zmienna)
n = 5
silnia = 1
for i in range (1,n+1,1):
    silnia = silnia * i
    
    print("wynik silnia = ",silnia )
    
Nazwafunkcji()
Nazwafunkcji()
Funkcjaargumentów(5)