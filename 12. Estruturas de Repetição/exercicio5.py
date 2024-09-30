#5) Escreva um programa que, a partir de um número inteiro digitado pelo usuário, mostre se o número é múltiplo de 2 e 3.

# Entrada de dados
numero = int(input("Digite um número inteiro: "))

# Verificação se o número é múltiplo de 2 e 3
if numero % 2 == 0 and numero % 3 == 0:
    print(f"O número {numero} é múltiplo de 2 e 3.")
else:
    print(f"O número {numero} NÃO é múltiplo de 2 e 3.")
