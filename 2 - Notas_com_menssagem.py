"""Faça um programa que receba duas notas, calcule e mostre a média aritmética e a
mensagem que se encontra na tabela a seguir:  
**************************************************
*           Tabela de Classificação               *
**************************************************
* Média Aritmética | Mensagem    *
*---------------------------------------------*
* 0,0 - 3,0         | Reprovado   *
* 3,0 - 7,0         | Exame       *
* 7,0 - 10,0        | Aprovado    *
**************************************************
"""

nota01 = float(input("Digite aqui sua primeira nota: "))
nota02 = float(input("Agora digite sua segunda nota aqui: "))

#processamento
media = (nota01+nota02)/2

if 0 <= media <= 3:
    print(f"Você foi reprovado, pois sua média foi de {media:.2f}.")

elif 3 <= media <= 7:
    print(f"Você ficou em exame substitutivo, pois sua média foi de {media:.2f}.")
else:
    print(f"Parabéns você foi aprovado, pois sua média foi de {media:.2f}.")