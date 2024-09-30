# 17) A partir de cinco números inteiros, digitados pelo usuário, determinar e exibir a quantidade de números que são pares.

# Entrada dos cinco números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))
num4 = int(input("Digite o quarto número inteiro: "))
num5 = int(input("Digite o quinto número inteiro: "))

# Inicializando a contagem de números pares
quantidade_pares = 0

# Verificando cada número se é par
if num1 % 2 == 0:
    quantidade_pares += 1

if num2 % 2 == 0:
    quantidade_pares += 1

if num3 % 2 == 0:
    quantidade_pares += 1

if num4 % 2 == 0:
    quantidade_pares += 1

if num5 % 2 == 0:
    quantidade_pares += 1

# Exibindo o resultado
print(f"A quantidade de números pares é: {quantidade_pares}")
