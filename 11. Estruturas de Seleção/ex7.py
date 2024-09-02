# 7) A partir de cinco números reais, digitados pelo usuário, exibir o valor da média considerando apenas os números que são maiores que zero e menores do que mil.


# Solicita cinco números reais do usuário
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))
num4 = float(input("Insira o quarto número: "))
num5 = float(input("Insira o quinto número: "))

# Inicializa variáveis para soma e contagem de números válidos
soma = 0
contador = 0

# += é o operador de adição com atribuição.
# Usando += (correto):
# x = 5
# x += 3  # Isso é o mesmo que: x = x + 3
# print(x)  # Saída: 8
# Usando =+ (incorreto):
# x = 5
# x =+ 3  # Isso é o mesmo que: x = +3 (atribui 3 a x)
# print(x)  # Saída: 3
# ou seja o + vem primeiro que o =

# Verifica se os números estão no intervalo (maiores que 0 e menores que 1000)

if 0 < num1 < 1000:
    soma += num1
    contador += 1
if 0 < num2 < 1000:
    soma += num2
    contador += 1
if 0 < num3 < 1000:
    soma += num3
    contador += 1
if 0 < num4 < 1000:
    soma += num4
    contador += 1
if 0 < num5 < 1000:
    soma += num5
    contador += 1

# Verifica se há números válidos para calcular a média
if contador > 0:
    media = soma / contador
    print(f"A média dos números válidos é {media}")
else:
    print("Nenhum número válido foi inserido (maior que 0 e menor que 1000).")

