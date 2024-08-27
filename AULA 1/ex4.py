#4) Criar uma aplicação que receba três números reais digitados pelo usuário e em seguida calcule e exiba a valor da média.

# Solicita três números reais do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Calcula a média dos números
media = (num1 + num2 + num3) / 3

# Exibe o resultado da média
print(f"A média dos números é: {media}")
