import math

# Função para calcular as raízes da equação do 2º grau
def calcular_bhaskara(a, b, c):
    # Calculando o discriminante (delta)
    delta = b**2 - 4*a*c

    # Verificando se o delta é negativo (não há raízes reais)
    if delta < 0:
        return "A equação não possui raízes reais."
    
    # Calculando as duas raízes
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    
    return (x1, x2)

# Função principal para receber os coeficientes e exibir as raízes
def resolver_equacao():
    print("Resolução de uma equação do 2º grau ax² + bx + c = 0")

    # Entrada dos coeficientes
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    # Chamando a função para calcular as raízes
    resultado = calcular_bhaskara(a, b, c)

    # Exibindo o resultado
    if isinstance(resultado, tuple):
        print(f"As raízes da equação são: x1 = {resultado[0]} e x2 = {resultado[1]}")
    else:
        print(resultado)

# Chama a função principal
resolver_equacao()
