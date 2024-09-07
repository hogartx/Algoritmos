# 13) Elaborar um programa de realize a conversão entre metros, pés, polegadas e milhas adotando, como referência que 1 polegada = 25.4 Milímetros, 1 pé = 30.48 Centímetros e 1 Milha = 1609.344 metros.

# Fatores de conversão
polegada_para_metros = 0.0254  # 1 polegada = 0.0254 metros
pe_para_metros = 0.3048       # 1 pé = 0.3048 metros
milha_para_metros = 1609.344   # 1 milha = 1609.344 metros

# Função para realizar a conversão
def converter(valor, unidade_origem, unidade_destino):
    # Converter a unidade de origem para metros
    if unidade_origem == 'metros':
        valor_metros = valor
    elif unidade_origem == 'pés':
        valor_metros = valor * pe_para_metros
    elif unidade_origem == 'polegadas':
        valor_metros = valor * polegada_para_metros
    elif unidade_origem == 'milhas':
        valor_metros = valor * milha_para_metros
    else:
        return None
    
    # Converter de metros para a unidade de destino
    if unidade_destino == 'metros':
        return valor_metros
    elif unidade_destino == 'pés':
        return valor_metros / pe_para_metros
    elif unidade_destino == 'polegadas':
        return valor_metros / polegada_para_metros
    elif unidade_destino == 'milhas':
        return valor_metros / milha_para_metros
    else:
        return None

# Entrada do usuário
unidade_origem = input("Digite a unidade de origem (metros, pés, polegadas, milhas): ").lower()
unidade_destino = input("Digite a unidade de destino (metros, pés, polegadas, milhas): ").lower()
valor = float(input(f"Digite o valor a ser convertido de {unidade_origem}: "))

# Realiza a conversão
valor_convertido = converter(valor, unidade_origem, unidade_destino)

# Exibe o resultado da conversão
if valor_convertido is not None:
    print(f"Resultado: {valor:.2f} {unidade_origem} equivalem a {valor_convertido:.2f} {unidade_destino}")
else:
    print("Unidade de origem ou destino inválida.")
