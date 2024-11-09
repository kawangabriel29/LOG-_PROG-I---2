"""
Uma agência bancária possui dois tipos de investimentos, conforme o quadro a seguir.
Faça um programa que receba o tipo de investimento e seu valor, calcule e mostre o valor
corrigido após um mês de investimento, de acordo com o tipo de investimento.

* TIPO  |  DESCRIÇÂO  | RENDIMENTO MENSAL *
* ----- | ----------- | ----------------- *
*   1   |  POUPANÇA   |        3%         *
* ----- | ----------- | ----------------- *
*   2   | RENDA FIXA  |        4%         *
* --------------------------------------- *
"""

#Valor e Tipo
valor_inv = float(input("Valor à ser investdo: "))
tipo_inv = int(input("Digite o tipo: "))

#Tipo de investimento
inv1 = valor_inv + (valor_inv * 0.03)
inv2 = valor_inv + (valor_inv * 0.04)

if tipo_inv == 1:
    print(f"O valor do seu investimento inicial após um mês é de: {inv1:.2f}.")
elif tipo_inv == 2:
    print(f"O valor do seu investimento inicial após um mês é de: {inv2:.2f}.")
else:
    print("Tipo de investimento não aceito!")



