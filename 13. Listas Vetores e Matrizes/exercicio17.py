# Variável para armazenar a soma dos números pares
soma = 0
# Variável para contar a quantidade de números pares
contagem = 0

# Laço para percorrer os números de 1 a 19
for numero in range(1, 20):
    if numero % 2 == 0:  # Verifica se o número é par
        soma += numero  # Soma os números pares
        contagem += 1  # Conta os números pares

# Calcula a média, se houver números pares
if contagem > 0:
    media = soma / contagem
    print(f"A média dos números pares entre 1 e 19 é: {media:.2f}")
else:
    print("Não há números pares no intervalo especificado.")
