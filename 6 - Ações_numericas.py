#Software actions mat.

print()
print(" --- Olá, seja bem vindo ao Actions Mat! ---")
print()
print(" Software feito para promover ações matematicas entre dois números")
print("\n Funções do app: ")
print(" 1 - Média entre os números\n 2 - Diferença do maior para o menor\n 3 - Produto entr os números\n 4 - Divisão do primeiro número com o segundo.")
print()
num_1 = float(input("Digite aqui seu primeiro numero: "))
num_2 = float(input("Digite aqui seu segundo numero: "))
print (" Opção 1 - Mostra a média dos números. \n Opção 2 - Mostra a diferença domaior para o menor. \n Opção 3 - Mostra a divisãodoprimeiro pelo segundo.")
op_usu = int(input("Digite a opção escolhida: "))

# OPÇÃO 1 - Média entre os números.
if op_usu == 1:
    media = (num_1+num_2)/2
    print(f"A média dos números é: {media}.")

# OPÇÃO 2 - Diferença do MAIOR pelo MENOR.
elif op_usu == 2:
     if num_1 > num_2: # SE for maior
          dif1 = (num_1 - num_2)
          print(f"A diferença de {num_1} (MAIOR) e {num_2} (MENOR), é: {dif1}.")
     else:
          dif2 = (num_2 - num_1) # SENÂO for maior, (MENOR)
          print(f"A diferença de {num_2} (MAIOR) e {num_1} (MENOR), é: {dif2}.")
    
# OPÇÃO 3 - Produto entre os números digitados.
elif op_usu == 3:
     prod = num_1 * num_2
     print(f"O produto dos dois números é: {prod}.")
    
#OPCÃO 4 - Divisão do primeiro pelo segundo.
elif op_usu == 4:
     div = num_1/num_2
     print(f"A divisão entre o primeiro número e o segundo é: {div}")

else:
    print("Opção inválida.")