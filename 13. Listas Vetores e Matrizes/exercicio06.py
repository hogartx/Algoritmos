# Solicita ao usuário um número entre 1 e 10
numero = int(input("Digite um número inteiro entre 1 e 10 para ver sua tabuada: "))

# Verifica se o número está dentro do intervalo válido
if 1 <= numero <= 10:
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):  # Gera os números de 1 a 10
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número inválido! Por favor, insira um número entre 1 e 10.")
