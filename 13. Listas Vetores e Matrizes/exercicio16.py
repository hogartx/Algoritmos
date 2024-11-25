# Variável para armazenar a soma dos números ímpares
soma = 0

# Laço para percorrer os números de 51 a 91
for numero in range(51, 92):  # O valor 92 é exclusivo, então vai até 91
    if numero % 2 != 0:  # Verifica se o número é ímpar
        soma += numero  # Soma os números ímpares

# Exibe a soma dos números ímpares
print(f"A soma dos números ímpares entre 51 e 91 é: {soma}")
