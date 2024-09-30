# 18) Considerando três números inteiros, fornecidos pelo usuário, exibi-los em ordem crescente.

# Entrada dos três números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# Coloca os números em uma lista
numeros = [num1, num2, num3]

# Ordena a lista em ordem crescente
numeros.sort()

# Exibe os números em ordem crescente
print(f"Os números em ordem crescente são: {numeros[0]}, {numeros[1]}, {numeros[2]}")
