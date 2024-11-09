print("")
print(" - Produto 1 - 1001 (R$ 5.32) \n - Produto 2 - 1324 (R$ 6.45) \n - Produto 3 - 6548 (R$ 2.37) \n - Produto 4 - 0987 (R$ 5.32) \n - Produto 5 - 7623 (R$ 6.45)")
print("")

cod_input = int(input("Digite o codigo do produto: "))
quant = int(input("Digite a quantidade do produto: "))

if cod_input == '1001':
    preco = 5.32
    total = quant * preco
    print(f"O seu total é de: {total:.2f}.")

elif cod_input == '1324':
    preco = 6.45
    total = quant * preco
    print(f"O seu total é de: {total:.2f}.")

elif cod_input == '6548':
    preco = 2.37
    total = quant * preco
    print(f"O seu total é de: {total:.2f}.")

elif cod_input == '0987':
    preco = 5.32
    total = quant * preco
    print(f"O seu total é de: {total:.2f}.")

elif cod_input == '7623':
    preco = 6.45
    total = quant * preco
    print(f"O seu total é de: {total:.2f}.")

else:
    print("<>")

