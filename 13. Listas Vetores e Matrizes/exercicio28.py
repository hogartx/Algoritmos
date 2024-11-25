# Função para contar vogais e consoantes
def contar_vogais_e_consoantes():
    # Inicializa as variáveis para contar vogais e consoantes
    vogais = 0
    consoantes = 0

    # Loop para ler 10 letras
    for i in range(10):
        letra = input(f"Digite a {i+1}ª letra: ").lower()  # Lê a letra e converte para minúscula

        # Verifica se a letra é válida (se é uma letra do alfabeto)
        if letra.isalpha() and len(letra) == 1:
            if letra in 'aeiou':
                vogais += 1
            else:
                consoantes += 1
        else:
            print("Por favor, digite uma letra válida.")
            return  # Caso a entrada não seja uma letra válida, termina a execução
    
    # Exibe o resultado
    print(f"\nQuantidade de vogais: {vogais}")
    print(f"Quantidade de consoantes: {consoantes}")

# Chama a função para executar a contagem
contar_vogais_e_consoantes()
