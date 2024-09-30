# 25) O IPVA de um veículo é calculado tomando como base o valor do veículo, o combustível utilizado e o tipo do veículo que serão fornecidos pelo usuário. Em seguida, o IPVA será calculado como 4% do valor doveículo, no caso de automóveis movidos a gasolina ou flex. Já para carros movidos somente a etanol, eletricidade ou gás ou qualquer desses três combustíveis combinados, a alíquota é de 3%. Para motos, camionetes cabine simples e ônibus ou micro-ônibus a alíquota é de 2% e para caminhões, de 1,5%. Elaborar uma rotina que, a partir destas informações, calcule o mostre o valor do IPVA.

# Entrada de dados
valor_veiculo = float(input("Digite o valor do veículo: "))
combustivel = input("Digite o combustível (gasolina, etanol, eletricidade, gás, flex): ").lower()
tipo_veiculo = input("Digite o tipo do veículo (automóvel, moto, camionete, ônibus, caminhão): ").lower()

# Inicializa a alíquota
aliquota = 0.0

# Determina a alíquota com base no tipo e combustível do veículo
if tipo_veiculo == "automóvel":
    if combustivel in ["gasolina", "flex"]:
        aliquota = 0.04  # 4%
    elif combustivel == "etanol":
        aliquota = 0.03  # 3%
    elif combustivel in ["eletricidade", "gás"]:
        aliquota = 0.03  # 3%
elif tipo_veiculo == "moto":
    aliquota = 0.02  # 2%
elif tipo_veiculo == "camionete":
    if combustivel in ["gasolina", "flex"]:
        aliquota = 0.04  # 4%
    elif combustivel == "etanol":
        aliquota = 0.03  # 3%
    elif combustivel in ["eletricidade", "gás"]:
        aliquota = 0.03  # 3%
elif tipo_veiculo in ["ônibus", "micro-ônibus"]:
    aliquota = 0.02  # 2%
elif tipo_veiculo == "caminhão":
    aliquota = 0.015  # 1.5%

# Calcula o valor do IPVA
ipva = valor_veiculo * aliquota

# Exibe o resultado
print(f"O valor do IPVA é: R$ {ipva:.2f}")
