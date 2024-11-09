"""O preço ao consumidor de um carro novo é a soma do custo de fábrica com a
porcentagem do distribuidor e dos impostos, ambos aplicados ao custo de fábrica. As
porcentagens encontram-se na tabela a seguir. Faça um programa que receba o custo de
fábrica de um carro e mostre o preço ao consumidor."""
"""

* Entre R$ 12.000,00|                   |            *
*  e    R$ 25.000,00|         10        |     15     * 
* ------------------|-------------------|----------- *
* Acima R$ 25.000,00|         15        |     20     *
* ------------------|-------------------|----------- *
"""
#preço p/ comsumidor: (custo_fabrica + distribuidor + imposto)
custo_fabrica = float(input("Digite o valor de fabrica do carro aqui: "))

#condição
if custo_fabrica <= 12000:
    distribuidor = 0.05 * custo_fabrica
    impostos = 0 * custo_fabrica
    preco_cons = custo_fabrica + distribuidor + impostos
    print(f"O preço do carro é de: {preco_cons}")

elif 12000 <= custo_fabrica <= 25000:
    distribuidor = 0.1 * custo_fabrica
    impostos = 0.15 * custo_fabrica
    preco_cons = custo_fabrica + distribuidor + impostos
    print(f"O preço do carro é de: {preco_cons}")

else:
    distribuidor = 0.15 * custo_fabrica
    impostos = 0.20 * custo_fabrica
    preco_cons = custo_fabrica + distribuidor + impostos
    print(f"O preço do carro é de: {preco_cons}")
