# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:35:17 2021

@author: rawsk Alicja Pierzchała
"""


x = [41, 50, 1, 8]
print("zawartoć x = ",x)
n = 4
max = x[0]
koszyk = 0
i = 1
for i in range(0, n):
    if x[0]>x[1]:
        koszyk = x[1]
        print("koszyk",koszyk)
        x[1] = x[0]
        print("x1",x[1])
        print("x0",x[0])
        x[0] = koszyk
        print("x0",x[0])
        print("x1",x[1])
        print("wartoci posortowane x =",  x)
    if x[0]>x[2]:
            koszyk = x[2]
            print("koszyk",koszyk)
            x[2] = x[0]
            print("x2",x[2])
            print("x0",x[0])
            x[0] = koszyk
            print("x0",x[0])
            print("x2",x[2])
    if x[0]>x[3]:
        koszyk = x[3]
        print("koszyk",koszyk)
        x[3] = x[0]
        print("x3",x[3])
        print("x0",x[0])
        x[0] = koszyk
        print("x0",x[0])
        print("x3",x[3])
        print("wartoci posortowane x =",  x)
    if x[1]>x[2]:
        koszyk = x[2]
        print("koszyk",koszyk)
        x[2] = x[1]
        print("x2",x[2])
        print("x1",x[1])
        x[1] = koszyk
        print("x1",x[1])
        print("x2",x[2])
        print("wartoci posortowane x =",  x) 
    if x[1]>x[3]:
            koszyk = x[3]
            print("koszyk",koszyk)
            x[3] = x[1]
            print("x3",x[3])
            print("x1",x[1])
            x[1] = koszyk
            print("x1",x[1])
            print("x3",x[3])
            print("wartoci posortowane x =",  x)
    if x[2]>x[3]:
            koszyk = x[3]
            print("koszyk",koszyk)
            x[3] = x[2]
            print("x3",x[3])
            print("x2",x[2])
            x[2] = koszyk
            print("x2",x[2])
            print("x3",x[3])
            print("wartoci posortowane x =",  x )   
print("wartoci posortowane końcowe wyswietlenie x =",  x)       