# 11) A partir dos lados de um retângulo ou quadrado, digitados pelo usuário, elaborar uma rotina que calcule e exiba o valor da sua área e informe se o mesmo é um retângulo ou um quadrado. Lembrando que a área é obtida pela multiplicação da base (L) pela altura (A)

# Solicita os lados do retângulo/quadrado
base = float(input("Digite o valor da base (L): "))
altura = float(input("Digite o valor da altura (A): "))

# Calcula a área
area = base * altura

# Verifica se é um quadrado ou um retângulo
if base == altura:
    print(f"A figura é um quadrado e sua área é {area:.2f} unidades²")
else:
    print(f"A figura é um retângulo e sua área é {area:.2f} unidades²")
