# Lista para armazenar os números digitados
numeros = []

# Solicita 15 números inteiros ao usuário
for i in range(1, 16):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    numeros.append(numero)

# Determina o maior número
maior = max(numeros)

# Exibe o maior número
print(f"\nO maior número digitado foi: {maior}")
