"""Ler dois valores e imprimir uma das três mensagens a seguir:

● “Números iguais”, caso os números sejam iguais
● “Primeiro é maior”, caso o primeiro seja maior que o segundo;
● “Segundo maior”, caso o segundo seja maior que o primeiro
"""
#Entrada dos números:
valor1 = int(input("Digite seu primeiro valor aqui: "))
valor2 = int(input("Agora digite seu segundo valor: "))

#Condições:
if valor1 == valor2:
    print(f"Os valores {valor1} e {valor2} são iguais!")

elif valor1 > valor2:
    print(f"Primeiro valor {valor1} é maior")

else:
    print(f"O segundo valor {valor2} o é maior")


