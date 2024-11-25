# Função para desenhar o diamante
def desenhar_diamante(n):
    # Parte superior do diamante
    for i in range(1, n + 1, 2):  # Começa de 1 e vai até n, pulando de 2 em 2
        print(' ' * ((n - i) // 2) + '*' * i)  # Calcula espaços e imprime a linha com '*' 

    # Parte inferior do diamante
    for i in range(n - 2, 0, -2):  # Começa de n-2 e vai até 1, diminuindo de 2 em 2
        print(' ' * ((n - i) // 2) + '*' * i)  # Calcula espaços e imprime a linha com '*' 

# Solicita ao usuário que digite um número ímpar
numero_usuario = int(input("Digite um número inteiro ímpar: "))

# Chama a função para desenhar o diamante
desenhar_diamante(numero_usuario)
