sal_inicial = float(input("Digite aqui se salário: "))

#condições
if sal_inicial <= 300: #até 300
    porcentagem = 0.15

elif sal_inicial  <= 600: #até 600
    porcentagem = 0.10

elif sal_inicial <= 900:
    porcentagem = 0.05

else:
    porcentagem = 0

#processamento
aumento = sal_inicial * porcentagem
novo_salario = sal_inicial + aumento

print(novo_salario)