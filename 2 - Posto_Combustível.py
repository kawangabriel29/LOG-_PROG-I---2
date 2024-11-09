#Entradas:
tipo = input("Digite A ou G: ")
litros = float(input("Quantiade de litros: "))

#Variáveis:
#definir valores dos combustiveis
valor_A = 3.90
valor_G = 5.30

#cáculo para o total sem desconto:
total_A = valor_A*litros
total_G = valor_G*litros

#Condições:
if tipo == 'A': 
    if litros <= 20:
        desconto = 0.03
        total_fim = total_A - (total_A*desconto)
        print(f"Seu total com desconto é de: {total_fim:.2f}.")
    else:
        desconto = 0.05
        total_fim = total_A - (total_A*desconto)
        print(f"Seu total com desconto é de: {total_fim:.2f}.")

elif tipo == 'G':
    if litros <= 20:
        desconto = 0.04
        total_fim = total_G - (total_G*desconto)
        print(f"Seu total com desconto é de: {total_fim:.2f}.")
    else:
        desconto = 0.06
        total_fim = total_G - (total_G*desconto)
        print(f"Seu total com desconto é de: {total_fim:.2f}.")

else:
    print("<><><>")
