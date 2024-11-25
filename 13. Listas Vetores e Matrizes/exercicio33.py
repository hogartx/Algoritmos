# Função para exibir o retângulo com as bordas
def exibir_retangulo():
    # Solicita ao usuário a quantidade de linhas e colunas
    linhas = int(input("Linhas? "))
    colunas = int(input("Colunas? "))

    # Exibe a linha superior com os sinais de "+"
    print("+" + "-" * (colunas - 2) + "+")

    # Exibe as linhas intermediárias com os sinais "|"
    for i in range(linhas - 2):
        print("|" + " " * (colunas - 2) + "|")
    
    # Exibe a linha inferior com os sinais de "+"
    print("+" + "-" * (colunas - 2) + "+")

# Chama a função para executar a exibição do retângulo
exibir_retangulo()
