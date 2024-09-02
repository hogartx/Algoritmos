# 2) Especificar uma aplicação que faça a leitura do nome e ano de nascimento de uma pessoa, calcule sua idade e exiba a idade calculada também indicando se a pessoa é maior ou menor de idade.

import time

# Solicita o nome do usuário
nome = input("Digite o seu nome: ")

# Solicita o ano de nascimento do usuário e converte para um número inteiro
anoNasc = int(input("Digite o ano de nascimento: "))

# Obtém o ano atual (o Y é abreviação de Year que signfica ano em inglês)
anoAtual = int(time.strftime("%Y"))

# Calcula a idade
idade = anoAtual - anoNasc

# Determina se o usuário é maior ou menor de idade
if idade >= 18:
    maioridade = "maior"
else:
    maioridade = "menor"

# Exibe o resultado
print(nome, ", a sua idade é", idade, "anos e você é", maioridade, "de idade")
