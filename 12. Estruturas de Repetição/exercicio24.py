# 24) A área de um triângulo (A) é definida pela metade do produto da altura (H) pela respectiva base (B). Escrever um programa que, a partir dos valores da altura e base, que deverão ser valores reais e maiores que zero digitados pelo usuário, realize o cálculo e exiba o valor da área.

# Entrada dos valores da altura e da base
altura = float(input("Digite o valor da altura (H): "))
base = float(input("Digite o valor da base (B): "))

# Verificando se os valores são maiores que zero
if altura > 0 and base > 0:
    # Cálculo da área do triângulo
    area = (base * altura) / 2
    
    # Exibindo o resultado
    print(f"A área do triângulo é: {area:.2f}")
else:
    print("A altura e a base devem ser maiores que zero.")
