# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:09:25 2021

@author: rawsk
"""


# x=[9,4,7,3,1]
# print(x)
# n = len(x)
# print("ilosc elementow = ",n)
# for i in range(0,n-1):
#     print("i", i)
#     for j in range(i+1, n):
#         print("j", j)
#         if x[i] > x[j]:
#             pom = x[i]
#             x[i] = x[j]
#             x[j] = pom
            
# print(x)

# def sortowanie(lista):
#     n = len(lista)
#     for i in range(0, n-1):
#         for j in range(i+1, n):
#             pom = lista[i]:
#             lista[i] = lista[j]
#             lista[j] = pom

# x = [9,4,7,3,1]   
# print("lista x:", x)    
# sortowanie(x)          
# print





# zmienna = input ("wprowadż liczbę i nacisnij enter    ")
# print("wprowadzono", zmienna)
# c = zmienna + " łańcuch "
# print("c"  ,c)


# zmienna = input ("wprowadż liczbę i nacisnij enter    ")
# print("wprowadzono", zmienna)
# c = int(zmienna) + 2
# print("c"  ,c)



class Student:
    def __init__(self, imie, nazwisko, pesel):
        self. imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.ocena = 5
    def przedstaw_sie(self):
            print(f"jestem{self.imie} {self.nazwisko}")
    def wyswietlNrPesel(self):
        return self.__pesel
            
obStudent1 = Student("Anna", "Kowalska", 123456)
obStudent2 = Student("Roman", "Nowak" 56789)

obStudent1.przedstaw_sie()
obStudent2.przedstaw_sie()
print("ocena studenta 1 =", obStudent1.ocena)
obStudent1.ocena = 6
print("ocena studenta 1 = ", obStudent1.ocena)
print("ocena studenta 2 = ", obStudent2.ocena)

print(obStudent1.__pesel)

        
        



