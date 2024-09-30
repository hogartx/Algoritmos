# 22) Elaborar uma rotina que determine e mostre a diferença entre o maior e o menor valor dentre quatro números reais fornecidos pelo usuário.

# Entrada dos quatro números reais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

# Inicializando as variáveis para o maior e menor número
maior = num1
menor = num1

# Verificando o maior número
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num4 > maior:
    maior = num4

# Verificando o menor número
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
if num4 < menor:
    menor = num4

# Calculando a diferença entre o maior e o menor número
diferenca = maior - menor

# Exibindo o resultado
print(f"A diferença entre o maior ({maior}) e o menor ({menor}) número é: {diferenca:.2f}")
