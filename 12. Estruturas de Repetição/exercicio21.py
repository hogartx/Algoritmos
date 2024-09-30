# 21) Considerando três nomes, digitados pelo usuário, exibi-los em ordem alfabética.

# Entrada dos três nomes
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")

# Coloca os nomes em uma lista
nomes = [nome1, nome2, nome3]

# Ordena a lista de nomes em ordem alfabética
nomes.sort()

# Exibe os nomes em ordem alfabética
print("Nomes em ordem alfabética:")
for nome in nomes:
    print(nome)
