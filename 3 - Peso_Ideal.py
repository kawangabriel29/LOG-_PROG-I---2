"""Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde h é a altura):
■ para homens: (72.7 * h) – 58.
■ para mulheres: (62.1 * h) – 44.7"""

alt = float(input("Olá, digite aqui sua altura em metros: "))
sexo = input("Digite aqui seu sexo: (m ou f):")

if sexo == "m":
    peso_ideal = (72.7 * alt) - 58
    print(f"Seu peso ideal é: {peso_ideal:.2f}.")

#Poderia sim já ir para o "else", porém quero que o usuario processe somente as letras "m" e "f", caso contrário exibe uma msg de erro.
elif sexo == "f":
    peso_ideal = (62.1 * alt) - 44.7
    print(f"Seu peso ideal é: {peso_ideal:.2f}.")

else:
    print("ERRO, Por favor digite M ou F.")