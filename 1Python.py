# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FPpnkY8UY1sEAS-65qiC02iu5wT1tK7W
"""

lista = []
for i in range (5):
  lista.append(int(input(f"Digite o {i + 1}° número: ")))

print("=-="*10)

for i in lista:
  if i % 2 == 0:
    print(f"{i} é número par")
  else:
    print(f"{i} é número ímpar")

print("=-="*10)

print(f"A média dos números acima é {sum(lista) / len(lista)}")