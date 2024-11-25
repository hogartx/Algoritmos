# Variáveis para armazenar o nome e preço do produto mais caro
produto_mais_caro = ""
preco_mais_caro = 0

# Laço para entrada de dados dos produtos
while True:
    # Solicita o nome do produto
    nome_produto = input("Digite o nome do produto: ")
    
    # Solicita o preço do produto
    preco_produto = float(input("Digite o preço do produto: R$ "))
    
    # Verifica se o preço do produto atual é o maior
    if preco_produto > preco_mais_caro:
        produto_mais_caro = nome_produto
        preco_mais_caro = preco_produto
    
    # Pergunta se deseja continuar
    continuar = input("Deseja digitar outro produto? (sim/não): ").strip().lower()
    
    if continuar != "sim":
        break

# Exibe o produto mais caro
print(f"\nO produto mais caro é: {produto_mais_caro} com o preço de R$ {preco_mais_caro:.2f}")
