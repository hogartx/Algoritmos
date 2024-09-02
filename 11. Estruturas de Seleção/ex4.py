# 4) Elaborar uma rotina que, a partir de um número real digitado pelo usuário, mostre o seu valor absoluto.

# Solicita um número real do usuário
numero_real = float(input("Digite um número real: "))


# if numero_real < 0:: Verifica se o número é negativo

# Se for negativo, valor_absoluto = -numero_real: Converte o número negativo em positivo ao multiplicar por -1

# Se não for negativo (ou seja, é zero ou positivo), valor_absoluto = numero_real: Mantém o número como está.

# O valor absoluto de um número representa a posição do número em relação ao zero, sem considerar se está à direita (positivo) ou à esquerda (negativo) do zero.

# Calcula o valor absoluto
if numero_real < 0:
    valor_absoluto = -numero_real
else:
    valor_absoluto = numero_real

# Exibe o valor absoluto
print("O valor absoluto de", numero_real, "é", valor_absoluto)
