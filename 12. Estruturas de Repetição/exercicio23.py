# 23) Desenvolver uma rotina que a partir de 5 letras digitadas pelo usuário, determine e mostre a quantidade de vogais.

# Entrada das cinco letras
letra1 = input("Digite a primeira letra: ").lower()
letra2 = input("Digite a segunda letra: ").lower()
letra3 = input("Digite a terceira letra: ").lower()
letra4 = input("Digite a quarta letra: ").lower()
letra5 = input("Digite a quinta letra: ").lower()

# Inicializando a variável para contar as vogais
vogais = 0

# Lista de vogais
lista_vogais = ['a', 'e', 'i', 'o', 'u']

# Verificando se cada letra é uma vogal
if letra1 in lista_vogais:
    vogais += 1
if letra2 in lista_vogais:
    vogais += 1
if letra3 in lista_vogais:
    vogais += 1
if letra4 in lista_vogais:
    vogais += 1
if letra5 in lista_vogais:
    vogais += 1

# Exibindo o resultado
print(f"Quantidade de vogais: {vogais}")
