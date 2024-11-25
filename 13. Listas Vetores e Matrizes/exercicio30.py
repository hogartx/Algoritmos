# Função para imprimir a sequência até a n-ésima linha
def imprimir_sequencia(n):
    # Loop que vai de 1 até o número n
    for i in range(1, n + 1):
        # Imprime o número i repetido i vezes
        print(" ".join([str(i)] * i))

# Solicita ao usuário o valor de n
n = int(input("Digite um número inteiro: "))

# Chama a função para imprimir a sequência
imprimir_sequencia(n)
