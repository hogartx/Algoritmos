# Exibindo números ímpares entre 101 e 121
print("Números ímpares entre 101 e 121:")
for numero in range(101, 122):  # Gera números de 101 a 121
    if numero % 2 != 0:  # Verifica se o número é ímpar
        print(numero)
