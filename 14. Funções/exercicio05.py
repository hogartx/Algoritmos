# Função para converter metros para polegadas
def metros_para_polegadas(metros):
    polegadas = metros * 39.3701  # 1 metro = 39,3701 polegadas
    return polegadas

# Função principal
def main():
    metros = float(input("Digite o valor em metros: "))  # Solicita ao usuário o valor em metros
    polegadas = metros_para_polegadas(metros)  # Chama a função para realizar a conversão
    print(f"{metros} metros equivalem a {polegadas:.2f} polegadas.")  # Exibe o resultado com 2 casas decimais

# Chama a função principal
main()
