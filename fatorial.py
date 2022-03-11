# -*- coding: utf-8 -*-
"""
Crie um programa que peça um número e calcule o seu fatorial

* for: 1
"""

fat = 1
n = int(input("n: "))
for x in range(1, n + 1):
    fat *= x
#fat = 0
#for i in range(n):
#fat *= x + 1
print(f"fat({n}) = {fat}")
