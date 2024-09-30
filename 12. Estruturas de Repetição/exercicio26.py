# 26) Elaborar um programa que calcule e exiba o comprimento de uma circunferência, a partir de um raio (R), digitado pelo usuário e que deverá ser um número real positivo. O comprimento é obtido através da fórmula: 2 x π x R.

import math  # Importa a biblioteca matemática para usar o valor de π

# Entrada do raio
raio = float(input("Digite o raio da circunferência (número real positivo): "))

# Verifica se o raio é positivo
if raio <= 0:
    print("Por favor, digite um número real positivo para o raio.")
else:
    # Cálculo do comprimento da circunferência
    comprimento = 2 * math.pi * raio

    # Exibindo o resultado
    print(f"O comprimento da circunferência é: {comprimento:.2f}")
