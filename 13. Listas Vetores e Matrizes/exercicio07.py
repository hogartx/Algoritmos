# Solicita os dois números ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Determina os limites do intervalo
inicio = min(num1, num2)  # Menor número
fim = max(num1, num2)  # Maior número

# Calcula a soma e a quantidade de números no intervalo
soma = 0
quantidade = 0

for numero in range(inicio, fim + 1):  # Inclui o número final no intervalo
    soma += numero
    quantidade += 1

# Calcula a média
media = soma / quantidade

# Exibe o resultado
print(f"A média dos números inteiros no intervalo de {inicio} a {fim} é {media:.2f}")
