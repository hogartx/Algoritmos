# Lista para armazenar os números digitados
numeros = []

# Solicita 10 números reais ao usuário
for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número real: "))
    numeros.append(numero)

# Determina o maior e o menor número
maior = max(numeros)
menor = min(numeros)

# Calcula a diferença entre o maior e o menor número
diferenca = maior - menor

# Exibe o valor da diferença
print(f"\nA diferença entre o maior e o menor número é: {diferenca:.2f}")
