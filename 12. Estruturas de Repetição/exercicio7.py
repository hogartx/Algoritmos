# 7) Criar um programa que permita ao usuário digitar dois números reais e uma das quatro operações matemáticas básicas e, em seguida, exiba o resultado do cálculo efetuado. A aplicação também não poderá permitir a tentativa de divisão de um número por zero.

# Solicita dois números reais do usuário
numero1 = float(input("Digite o primeiro número real: "))
numero2 = float(input("Digite o segundo número real: "))

# Solicita a operação matemática desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# ATENÇÃO em Python, = e == são usados para propósitos diferentes e têm significados distintos.

# Função: O operador = é usado para atribuir um valor a uma variável.
# Exemplo:
# x = 10
# O operador == é usado para comparar dois valores e verificar se eles são iguais.
#Exemplo:
#   x = 10 
#   y = 5
#       if x == y:
#    print("x é igual a y")
# else:
#    print("x não é igual a y")
#
# Neste exemplo, x (que tem o valor 10) é comparado com y (que tem o valor 5). Como 10 não é igual a 5, a condição x == y é falsa e a mensagem "x não é igual a y" será impressa.


# Verifica e realiza o cálculo de acordo com a operação escolhida.
if operacao == '+':
    resultado = numero1 + numero2
    print("Resultado:", resultado)
elif operacao == '-':
    resultado = numero1 - numero2
    print("Resultado:", resultado)
elif operacao == '*':
    resultado = numero1 * numero2
    print("Resultado:", resultado)
elif operacao == '/':

# Verifica se o divisor é zero, se for então a operação não será efetuada.
    if numero2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = numero1 / numero2
        print("Resultado:", resultado)

# else: Se a operação fornecida não for uma das opções válidas, exibe uma mensagem de erro.
else:
    print("Operação inválida. Por favor, escolha uma das operações: +, -, *, /.")
