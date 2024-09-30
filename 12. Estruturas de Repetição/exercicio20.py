# 20) A partir de quatro números inteiros, inseridos pelo usuário, exibir a quantidade de números que são múltiplos de 5, maiores ou iguais a 100 e menores do que 200.

# Entrada dos quatro números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))
num4 = int(input("Digite o quarto número inteiro: "))

# Inicializa a variável para contar os números que atendem aos critérios
contador = 0

# Verifica cada número
if num1 % 5 == 0 and 100 <= num1 < 200:
    contador += 1

if num2 % 5 == 0 and 100 <= num2 < 200:
    contador += 1

if num3 % 5 == 0 and 100 <= num3 < 200:
    contador += 1

if num4 % 5 == 0 and 100 <= num4 < 200:
    contador += 1

# Exibe o resultado
print(f"Quantidade de números que são múltiplos de 5 e estão entre 100 e 200: {contador}")
