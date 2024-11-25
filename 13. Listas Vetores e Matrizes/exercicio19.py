# Função para contar múltiplos de 7 em um intervalo
def contar_multiplos_de_7(inicio, fim):
    # Variável para contar os múltiplos de 7
    contagem = 0
    # Laço para percorrer o intervalo fornecido
    for numero in range(inicio, fim + 1):  # Inclui o 'fim' no intervalo
        if numero % 7 == 0:  # Verifica se o número é múltiplo de 7
            contagem += 1  # Incrementa a contagem
    return contagem

# Solicita ao usuário o intervalo
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

# Chama a função para contar os múltiplos de 7 no intervalo
quantidade = contar_multiplos_de_7(inicio, fim)

# Exibe a quantidade de múltiplos de 7
print(f"A quantidade de múltiplos de 7 entre {inicio} e {fim} é: {quantidade}")
