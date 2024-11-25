# Variável para armazenar a soma dos números divisíveis por 3
soma = 0
contador = 0

# Solicita 10 números divisíveis por 3
while contador < 10:
    numero = int(input("Digite um número divisível por 3: "))
    
    # Verifica se o número é divisível por 3
    if numero % 3 == 0:
        soma += numero  # Soma o número à variável soma
        contador += 1    # Conta os números válidos
    else:
        print("O número não é divisível por 3. Tente novamente.")

# Exibe o resultado da soma
print(f"\nA soma dos 10 números divisíveis por 3 é: {soma}")
