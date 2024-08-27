#2) Elaborar um programa que realize a multiplicação de dois valores numéricos do tipo de dado real digitados pelo usuário e, depois, exiba o valor calculado

# input() captura os valores inseridos pelo usuário.
# float() converte os valores digitados em números reais.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a multiplicação dos números
resultado = num1 * num2

# Exibe o resultado da multiplicação
print(f"O resultado da multiplicação é: {resultado}")
