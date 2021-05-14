# -*- coding: utf-8 -*-
"""
Created on Sat May  8 12:19:14 2021

@author: rawsk
"""


# a = 7
# b = 1
# suma = 0
# ile = 0
# srednia = 0
# liczba = 0

# for ile in range (0,2):
#     if a % 2 == 0:
#         liczba = a
#         suma = suma + liczba
#         print("suma = ",suma)
#         ile = ile + 1
#     #continue 
#         liczba + liczba + 1
#         liczba <= b: 
#         srednia = suma / ile
#             print("Średnia = ", srednia)
  
# print("liczba", liczba)
# print("suma= " )
# print("srednia = ", srednia)    

def Nazwafunkcji():
    print("wynik funkcji")
    print("końcowy wynik")

def Funkcjaargumentów (zmienna):
    print("podałam zmienną która wynosi = ", zmienna)

a = 2
b = 2
n = 0
srednia = 0
for i in range (1,2):
    if a % 2 == 0:
        print ("a jest liczba parzysta")
    if b % 2 == 0: 
            print ("b jest liczba parzysta")
            n = a + b 
            i = i + 1
            print ("wielkosc i = ", i)
            srednia = n / i
            print("suma= ",n )
            print("srednia = ", srednia)
    else :
        print("Prodram nie zadziała, jesli a i b jest liczną nieparzystą !!!")
        

    