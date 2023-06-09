# -*- coding: utf-8 -*-
"""3Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18jYYcEvC_DX6oE8HKhd3XALyN4cv6-KB
"""

"""
3 - Elabore um programa de computador
que realize o cálculo de notas. Este
programa deverá solicitar o nome do aluno
e quatro notas, todo este conjunto deverá
estar contido em um laço que confirme se
deseja encerrar o programa ou continuar
solicitando outros nomes e notas.
Ao final da solicitação do nome e das
notas deverá ser impresso o nome do
aluno e a sua média, se a nota for menor
que 6 imprimir Reprovado, senão, se a
nota for igual ou maior que 6, imprimir
Aprovado
"""

nomes = []
notas = []
medias = []
continuar = ""

while True:
  if continuar == "N":
    break
  else:
    nome = input("Nome do Aluno: ")
    nomes.append(nome)
    print("-")
    for i in range(4):
      nota = -1
      while nota < 0 or nota > 10:
        nota = float(input(f"Digite a {i + 1}° nota (0 a 10): "))
        if nota < 0 or nota > 10:
          print("Valor Inválido! Notas entre 0 e 10")
          continue
        else:
          notas.append(nota)

    medias.append(sum(notas) / len(notas))
    notas = []
    continuar = ""
    print("=-="*8)

    while continuar != "S" and continuar != "N":
      continuar = input("Deseja continuar a aplicar notas? S ou N: ")
      if continuar == "S":
        print("=-="*8)
        break
      elif continuar == "N":
        break
      else:
        print("-")
        print("Valor Inválido! Digite S ou N")
        print("-")
        continuar = ""

print("=-="*8)

for i in range(len(nomes)):
  if medias[i] < 6:
    print(f"O aluno {nomes[i]} obteve a média de {medias[i]}, assim, sendo Reprovado!")
  else:
    print(f"O aluno {nomes[i]} obteve a média de {medias[i]}, assim, sendo Aprovado!")
  print("-")