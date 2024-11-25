# Função para calcular a sequência de Fibonacci
def fibonacci(n):
    sequencia = [1, 2]  # Começa com os dois primeiros números da sequência
    while len(sequencia) < n:
        # O próximo número é a soma dos dois últimos da sequência
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

# Definir a quantidade de números que queremos (neste caso, 6)
quantidade = 6

# Chamar a função e obter os 6 primeiros números da sequência
sequencia_fibonacci = fibonacci(quantidade)

# Exibir a sequência
print(f"Os {quantidade} primeiros números da sequência de Fibonacci são: {sequencia_fibonacci}")
