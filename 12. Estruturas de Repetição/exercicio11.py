# 11) Elaborar um programa que realize a resolução de uma equação do 2º grau utilizando, para isso, a Fórmula de Báskara.

# Solicita os coeficientes da equação ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcula o discriminante
delta = b**2 - 4*a*c

# Exibe o valor do discriminante
print(f"O valor de delta é: {delta:.2f}")

# Verifica o valor de delta e calcula as raízes
if delta > 0:
    # Duas raízes reais e distintas (usando **0.5 para a raiz quadrada)
    # Em Python, o operador ** é usado para elevar um número a uma potência. 
    # Quando elevamos um número à potência de 0.5, estamos calculando a sua raiz quadrada, pois a raiz quadrada de um número é o mesmo que elevá-lo à potência de 1/2.
    raiz1 = (-b + (delta ** 0.5)) / (2 * a)
    raiz2 = (-b - (delta ** 0.5)) / (2 * a)
    print(f"As raízes da equação são: {raiz1:.2f} e {raiz2:.2f}")
elif delta == 0:
    # Uma raiz real dupla
    raiz = -b / (2 * a)
    print(f"A raiz da equação é: {raiz:.2f}")
else:
    # Raízes complexas (calculando a parte imaginária com **0.5)
    parte_real = -b / (2 * a)
    parte_imaginaria = ((-delta) ** 0.5) / (2 * a)
    print(f"As raízes da equação são: {parte_real:.2f} + {parte_imaginaria:.2f}i e {parte_real:.2f} - {parte_imaginaria:.2f}i")

