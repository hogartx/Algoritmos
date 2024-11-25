# Função para calcular o produto dos números pares até o número fornecido
def produto_pares(numero):
    produto = 1  # Inicializa o produto com 1 (neutro para multiplicação)
    
    # Laço para percorrer os números de 1 até o número fornecido
    for i in range(2, numero + 1, 2):  # Começa de 2 e vai até o número fornecido (com passo 2)
        produto *= i  # Multiplica o número par ao produto
    
    return produto

# Solicita ao usuário que digite um número
numero_usuario = int(input("Digite um número inteiro: "))

# Chama a função e calcula o produto dos números pares até o número fornecido
resultado_produto = produto_pares(numero_usuario)

# Exibe o resultado
print(f"O produto dos números pares de 1 até {numero_usuario} é: {resultado_produto}")
