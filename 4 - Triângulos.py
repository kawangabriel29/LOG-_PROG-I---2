"""Fazer um algoritmo para ler 3 valores numéricos (A, B, e C) e escrever se esses valores formam
um triângulo equilátero, isósceles ou escaleno. No caso dos valores não formarem um triângulo,
escrever uma mensagem sobre isso."""

#entrada
a = int(input("Digite seu primeiro número aqui: "))
b = int(input("Digite seu segundo número aqui: "))
c = int(input("Digite seu terceiro número aqui: "))

#verificar se forma um triangulo
if a+b>c or a+c>b or b+c>a:
    if a == b == c:
        print("Equilátero: Todos os lados são iguais.")
    elif a == b or a == c or b == c:
        print("Isósceles: Dois lados são iguais.")
    else:
        print("Escaleno: Todos os lados são diferentes.")
else:
    print("Esses vaores nao formas um triângulo")