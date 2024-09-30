# 3) Escreva um programa que, a partir de um número inteiro digitado pelo usuário, mostre se o número é par ou ímpar.

# Solicita um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))


# O operador % é conhecido como operador módulo (ou operador de resto). Ele retorna o resto da divisão inteira entre dois números.

# if numero % 2 == 0: Usa o operador módulo % para verificar o resto da divisão do número por 2. Se o resto for 0, o número é par.

# else: Se o resto não for 0, o número é ímpar.

# todo múltiplo de 2 é par então se o resto for igual a 0 quer dizer que o número é divisível por 2 (par).


# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")
