# Variável para contar os múltiplos de 4
contagem = 0

# Laço para percorrer os números entre 40 e 80
for numero in range(40, 81):  # O intervalo vai de 40 até 80, inclusive
    if numero % 4 == 0:  # Verifica se o número é múltiplo de 4
        contagem += 1  # Incrementa a contagem

# Exibe a quantidade de múltiplos de 4
print(f"A quantidade de números múltiplos de 4 entre 40 e 80 é: {contagem}")
