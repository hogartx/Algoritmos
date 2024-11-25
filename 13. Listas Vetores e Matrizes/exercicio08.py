# Lista para armazenar os números digitados
numeros = []

# Solicita 10 números reais ao usuário
for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número real: "))
    numeros.append(numero)

# Determina o menor número
menor = min(numeros)

# Exibe o menor número
print(f"\nO menor número digitado foi: {menor}")
