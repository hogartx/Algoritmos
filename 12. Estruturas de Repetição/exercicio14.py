# 14) A partir de um valor digitado pelo usuário e o respectivo prefixo mostrar a representação do valor nos demais prefixos, por exemplo:
#
# Entrada:
# +-----------------------------------------------------+
# | Digite o valor: 10.000                            |
# | Digite o prefixo: M                              |
# +-----------------------------------------------------+
#
# Saída:
# +----------------------------------------------+
# | Entrada:                                    |
# | Digite o valor: 10.000.000                  |
# | Digite o prefixo: k                         |
# +----------------------------------------------+                              
# | 10.000.000 k                   |
# | 10 G
# | 0,01 T                        |
# +----------------------------------------------+
#
# Adotar, como referência a tabela mostrada a seguir:
#
#
# +----------------------------------------------+
# | Prefixo | Valor (Decimal)                    |
# +----------------------------------------------+
# | k       | 10^3 (1000)                       |
# | M       | 10^6 (1,000,000)                   |
# | G       | 10^9 (1,000,000,000)               |
# | T       | 10^12 (1,000,000,000,000)         |
# +----------------------------------------------+


# Dicionário com os valores decimais correspondentes a cada prefixo
prefixos = {
    'k': 10**3,
    'M': 10**6,
    'G': 10**9,
    'T': 10**12
}

# Entrada de dados
valor = float(input("Digite o valor: "))
prefixo = input("Digite o prefixo (k, M, G, T): ").strip()

# Verifica se o prefixo digitado é válido
if prefixo not in prefixos:
    print("Prefixo inválido!")
else:
    # Converte o valor para a unidade base (sem prefixo)
    valor_base = valor * prefixos[prefixo]

    # Exibe o valor correspondente em cada prefixo
    for p, fator in prefixos.items():
        valor_convertido = valor_base / fator
        print(f"{valor_convertido:.3f} {p}")

