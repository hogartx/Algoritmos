# 19) Elaborar uma rotina que, a partir de quatro números inteiros que deverão ser digitados pelo usuário, determine e mostre o maior número par.

# Entrada dos quatro números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))
num4 = int(input("Digite o quarto número inteiro: "))

# Inicializa a variável para o maior número par
maior_par = None

# Verifica se os números são pares e atualiza o maior_par
if num1 % 2 == 0:
    maior_par = num1

if num2 % 2 == 0:
    if maior_par is None or num2 > maior_par:
        maior_par = num2

if num3 % 2 == 0:
    if maior_par is None or num3 > maior_par:
        maior_par = num3

if num4 % 2 == 0:
    if maior_par is None or num4 > maior_par:
        maior_par = num4

# Verifica se algum número par foi encontrado
if maior_par is not None:
    print(f"O maior número par é: {maior_par}")
else:
    print("Nenhum número par foi encontrado.")
