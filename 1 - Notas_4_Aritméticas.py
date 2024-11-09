"""programa que receba quatro notas de um aluno, calcule e mostre a média
aritmética das notas e a mensagem de aprovado ou reprovado, considerando para
aprovação média 7"""

#Entrada
nota1 = float(input("Digite aqui sua primeira nota: "))
nota2 = float(input("Digite aqui sua segunda nota: "))
nota3 = float(input("Digite aqui sua terceira nota: "))
nota4 = float(input("Digite aqui sua quarta nota: "))

#Processamento / Arimtmetica: soma os valorrs e divide pela quantidade de valores.
media = (nota1+nota2+nota3+nota4)/4

#condicinais
if media >= 7:
    print(f"Parabéns você foi aprovado com {media:.2f} de média.")
else:
    print(f"Infelizmente você não foi aprovado. sua média foi de {media:.2f}.")


