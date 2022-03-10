# -*- coding: utf-8 -*-
"""
Crie um programa que peça dois números para o usuário e mostre o qual é o maior deles.

* if: 0
"""

a = int(input("a: "))
b = int(input("b: "))
if a > b:
    print(f"o maior numero e o a = {a}")
elif b > a:
    print(f"o maior numero e o b = {b}") 
else:
    print(f"os numeros sao iguais")
#elif a > b:
#if b > a:
