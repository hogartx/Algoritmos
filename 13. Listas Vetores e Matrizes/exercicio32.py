# Função para exibir o caractere nas linhas e colunas fornecidas
def exibir_caractere():
    # Solicita ao usuário a quantidade de linhas, colunas e o caractere
    linhas = int(input("Linhas? "))
    colunas = int(input("Colunas? "))
    caractere = input("Caractere? ")

    # Exibe o caractere repetido nas linhas e colunas solicitadas
    for i in range(linhas):
        print(caractere * colunas)

# Chama a função para executar a exibição
exibir_caractere()
