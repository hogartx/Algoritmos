# Função para identificar o produto mais caro
def produto_mais_caro():
    # Inicializa as variáveis para armazenar o nome e preço do produto mais caro
    nome_mais_caro = ""
    preco_mais_caro = 0

    # Loop para digitar os 10 produtos
    for i in range(10):
        nome = input(f"Digite o nome do {i+1}º produto: ")
        preco = float(input(f"Digite o preço do {i+1}º produto: R$ "))
        
        # Verifica se o preço do produto atual é maior que o do produto mais caro
        if preco > preco_mais_caro:
            preco_mais_caro = preco
            nome_mais_caro = nome

    # Exibe o nome do produto mais caro
    print(f"\nO produto mais caro é {nome_mais_caro}, com o preço de R$ {preco_mais_caro:.2f}")

# Chama a função para identificar o produto mais caro
produto_mais_caro()
