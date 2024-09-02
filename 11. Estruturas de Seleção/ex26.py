# 26) Desenvolver um programa para uma loja que precisa determinar o preço final de uma compra, a partir dos seguintes dados fornecidos pelo usuário: código, descrição, peso, quantidade e preço. Em seguida, para determinar o preço final, devem-se utilizar os seguintes critérios para cálculo:
#
# a) O preço total (bruto) é obtido multiplicando o preço unitário com a quantidade;
#
# b) O valor do imposto será obtido através das seguintes faixas:
# +-----------------------------------------+
# | Preço total (bruto)      | Valor do Imposto        |
# +-----------------------------------------+
# | < R$ 500,00              | 5,0% do preço total     |
# | >= R$ 500,00 e < R$ 1.500,00 | 7,5% do preço total |
# | >= R$ 1.500,00          | 10,0% do preço total    |
# +-----------------------------------------+
#
# c) Quando o peso total do produto (peso x quantidade) for maior que 10kg acrescentar R$ 50,00 de custo de frete, caso contrário, o frete será gratuito;
#
# d) O preço final será obtido somando o preço total (bruto) com o valor do imposto e o custo do frete.
#
#
