# -*- coding: utf-8 -*-
"""
Crie um programa que mostre a quantidade de dígitos que a soma de dois números 
inteiros possui 

* int: 1
"""

a = int(input("a: "))
b = int(input("b: "))
c = a + b
n = 0
div = 10

while c:
    c = c // div
    n += 1
print(f"número de dígitos = {n}")

#c = c % div
#n += div
#div = 2
#print(f"soma = {c}")
#c = a + b
