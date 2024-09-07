# 12) Considerando a moeda Real, Dólar Americano e Euro elaborar uma rotina na qual o usuário irá digitar o valor, a respetiva moeda e a moeda para a qual deseja converter o valor. Em seguida, o programa deverá calcular o exibir o valor convertido, por exemplo:
# ENTRADA:
# +-----------------------------------------------------+
# | Digite a moeda: US$                               |
# | Digite o valor: 100,00                            |
# | Digite a moeda para qual deseja realizar a       |
# | conversão: R$                                     |
# +-----------------------------------------------------+
# SAÍDA:
# +-----------------------------------------------------+
# | Resultado: R$ 245,00  
# +-----------------------------------------------------+
#
# Importante: Obter a cotação das moedas no dia da resolução do exercício.

# Definir as cotações (valores fictícios para o exemplo)
cotacao_dolar_para_real = 4.90  # 1 dólar = 4.90 reais
cotacao_euro_para_real = 5.30   # 1 euro = 5.30 reais
cotacao_real_para_dolar = 1 / cotacao_dolar_para_real  # 1 real = 1/4.90 dólares
cotacao_real_para_euro = 1 / cotacao_euro_para_real    # 1 real = 1/5.30 euros
cotacao_dolar_para_euro = 0.90  # 1 dólar = 0.90 euros
cotacao_euro_para_dolar = 1 / cotacao_dolar_para_euro  # 1 euro = 1/0.90 dólares

# Função para realizar a conversão de moeda
def converter_moeda(valor, moeda_origem, moeda_destino):
    if moeda_origem == 'R$' and moeda_destino == 'US$':
        return valor * cotacao_real_para_dolar
    elif moeda_origem == 'R$' and moeda_destino == '€':
        return valor * cotacao_real_para_euro
    elif moeda_origem == 'US$' and moeda_destino == 'R$':
        return valor * cotacao_dolar_para_real
    elif moeda_origem == '€' and moeda_destino == 'R$':
        return valor * cotacao_euro_para_real
    elif moeda_origem == 'US$' and moeda_destino == '€':
        return valor * cotacao_dolar_para_euro
    elif moeda_origem == '€' and moeda_destino == 'US$':
        return valor * cotacao_euro_para_dolar
    else:
        return None

# Entrada do usuário
moeda_origem = input("Digite a moeda de origem (R$, US$, €): ")
valor = float(input("Digite o valor a ser convertido: "))
moeda_destino = input("Digite a moeda para qual deseja realizar a conversão (R$, US$, €): ")

# Realiza a conversão
valor_convertido = converter_moeda(valor, moeda_origem, moeda_destino)

# Exibe o resultado da conversão
if valor_convertido is not None:
    print(f"Resultado: {moeda_destino} {valor_convertido:.2f}")
else:
    print("Conversão não disponível entre as moedas selecionadas.")
