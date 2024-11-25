# Função para calcular a soma dos primeiros n números da sequência de Fibonacci
def soma_fibonacci(n):
    a, b = 1, 2  # Os dois primeiros números da sequência de Fibonacci
    soma = a + b  # Inicializa a soma com os dois primeiros números
    
    # Laço para calcular os próximos números e somá-los
    for _ in range(3, n + 1):  # Começa do 3º número até o n-ésimo
        a, b = b, a + b  # Atualiza a e b para os próximos números
        soma += b  # Adiciona o número b à soma
    
    return soma

# Definir a quantidade de números que queremos (neste caso, 10)
quantidade = 10

# Chama a função e obtém a soma dos 10 primeiros números da sequência
resultado_soma = soma_fibonacci(quantidade)

# Exibe a soma dos 10 primeiros números da sequência
print(f"A somatória dos {quantidade} primeiros números da sequência de Fibonacci é: {resultado_soma}")
