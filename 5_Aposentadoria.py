#ENTRADAS
cod_fun = int(input("Digite aqui seu código: "))
nasc = int(input("Digite aqui seu ano de nascimento: "))
entrada_empr = int(input("Digite o ano de entrada na empresa: "))

#Cálculos
ano_atual = 2024
idade = (ano_atual - nasc)
tempo_trabalho = (ano_atual - entrada_empr)

print("<>")

if idade >= 65 or (idade >= 60 and tempo_trabalho >= 25):
    print(f"Código do funcionário: {cod_fun}")
    print(f"Idade: {idade} anos")
    print(f"Tempo de trabalho: {tempo_trabalho} anos")
    print("Parabéns! Você atende aos requisitos para aposentadoria.")
else:
    print(f"Código do funcionário: {cod_fun}")
    print(f"Idade: {idade} anos")
    print(f"Tempo de trabalho: {tempo_trabalho} anos")
    print("Infelizmente, você ainda não atende aos requisitos para aposentadoria.")


"""if idade >= 65:
    if tempo_trabalho >= 30:
        print(f"codigo do fúncionario: {cod_fun}\nIdade: {idade}\nTempo de trabalho na empresa: {tempo_trabalho} anos\nVocê pode se aposentar.")

elif idade >= 60:
    if tempo_trabalho >= 25:
        print(f"codigo do fúncionario: {cod_fun}\nIdade: {idade}\nTempo de trabalho na empresa: {tempo_trabalho} anos\nVocê pode se aposentar.")

else:
    print(f"codigo do fúncionario: {cod_fun}\nIdade: {idade}\nTempo de trabalho na empresa: {tempo_trabalho} anos\nVocê não pode aposentar.")
"""
