# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:19:07 2021

@author: rawsk
"""

# nazwa_listy = ["jeden","drugi","trzeci","czwarty"]
# print(nazwa_listy)
# print("nazwa listy[0]: " ,nazwa_listy[0])

# lista_druga = [0, 8, 5, 2]
# print("nazwa listy [0]", lista_druga[0])
# print("nazwa listy [1]", lista_druga[1])
# print("nazwa listy [2]", lista_druga[2])
# print("nazwa listy [3]", lista_druga[3])

import matplotlib.pyplot as plt

n = 4
x = [3, 5, 7, 4]
max = x[0]
imax = 0
i = 1
for i in range(1, n):
    if x[i]>max :
        max = x[i]
        imax = i
        
plt.plot(x,'ro')
print("max", max)
print("imax",imax)


# print ("liczby w ciagu ", ciag)
# print("wartosć n", n)
# for n in range (0,4):
#     if ciag[n] > ciag[n+1]:
#        # wmax == ciag[]
#         n = n + 1
#     print("wartosc",ciag[n])