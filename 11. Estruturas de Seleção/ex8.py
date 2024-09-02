# 8) Para converter a temperatura de graus Celsius para Fahrenheit, utilizase a fórmula: F = C × 1,8 + 32. Elaborar uma rotina que realize essa conversão a partir de uma temperatura digitada pelo usuário.

# Solicita ao usuário a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Realiza a conversão para Fahrenheit usando a fórmula
fahrenheit = celsius * 1.8 + 32

# Exibe o resultado da conversão
print(f"A temperatura em Fahrenheit é: {fahrenheit:.1f} °F")
