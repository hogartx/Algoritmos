# Função para contar múltiplos de 2 e 3 no intervalo entre 1 e 100
def contar_multiplos_2_e_3(inicio, fim):
    # Inicializa a contagem
    contagem = 0
    
    # Laço para percorrer o intervalo
    for numero in range(inicio, fim + 1):
        # Verifica se o número é múltiplo de 2 e de 3
        if numero % 2 == 0 and numero % 3 == 0:
            contagem += 1  # Incrementa a contagem
    
    return contagem

# Definir o intervalo entre 1 e 100
inicio = 1
fim = 100

# Chama a função e obtém a contagem
quantidade = contar_multiplos_2_e_3(inicio, fim)

# Exibe a quantidade de múltiplos de 2 e 3
print(f"A quantidade de números múltiplos de 2 e de 3 entre {inicio} e {fim} é: {quantidade}")
