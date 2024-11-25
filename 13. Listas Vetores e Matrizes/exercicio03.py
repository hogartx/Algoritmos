# Solicita o intervalo ao usuário
inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

# Exibe os números inteiros no intervalo
print(f"Números inteiros entre {inicio} e {fim}:")
for numero in range(inicio, fim + 1):  # Inclui o limite superior
    print(numero)
