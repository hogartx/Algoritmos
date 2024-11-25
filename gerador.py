def criar_arquivos(nome, quantidade):
    for i in range(1, quantidade + 1):
        nome_arquivo = f"{nome}{i:02}.py"  # Nome do arquivo com numeração de dois dígitos
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("# Arquivo gerado automaticamente\n")
        print(f"Arquivo {nome_arquivo} criado com sucesso.")

# Exemplo de uso
nome = input("Digite o nome base do arquivo: ")
quantidade = int(input("Digite a quantidade de arquivos: "))
criar_arquivos(nome, quantidade)
