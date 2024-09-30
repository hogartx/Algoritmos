# 27) Desenvolver um programa para uma loja que precisa determinar o preço final de uma compra, a partir dos seguintes dados fornecidos pelo usuário: código, descrição, peso, quantidade e preço. Em seguida, para determinar o preço final, devem-se utilizar os seguintes critérios para cálculo:
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

# Entrada de dados
codigo = input("Digite o código do produto: ")
descricao = input("Digite a descrição do produto: ")
peso = float(input("Digite o peso do produto (kg): "))
quantidade = int(input("Digite a quantidade: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))

# Cálculo do preço total (bruto)
preco_total_bruto = preco_unitario * quantidade

# Cálculo do imposto
if preco_total_bruto < 500:
    imposto = 0.05 * preco_total_bruto  # 5% do preço total
elif 500 <= preco_total_bruto < 1500:
    imposto = 0.075 * preco_total_bruto  # 7,5% do preço total
else:
    imposto = 0.10 * preco_total_bruto  # 10% do preço total

# Cálculo do custo de frete
peso_total = peso * quantidade
if peso_total > 10:
    custo_frete = 50.00  # Frete de R$ 50,00
else:
    custo_frete = 0.00  # Frete gratuito

# Cálculo do preço final
preco_final = preco_total_bruto + imposto + custo_frete

# Exibindo o resultado
print("\n----- RESUMO DA COMPRA -----")
print(f"Código: {codigo}")
print(f"Descrição: {descricao}")
print(f"Peso: {peso} kg")
print(f"Quantidade: {quantidade}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Preço Total Bruto: R$ {preco_total_bruto:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Custo de Frete: R$ {custo_frete:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
