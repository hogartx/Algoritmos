# 15) Utilizando a mesma tabela do exercício anterior, elaborar uma rotina na qual o usuário irá digitar o valor, o respetivo prefixo e o prefixo para a qual deseja representar o valor. Em seguida, o programa deverá exibir a representação do valor, por exemplo:
#
# ENTRADA:
# +---------------------------------------------------------------+                                                     
# | Digite o valor: 1.000.000                                    |
# | Digite o prefixo: M                                          |
# | Digite o prefixo que deseja visualizar: T                    |
# +---------------------------------------------------------------+
#
#
# SAÍDA:
# +---------------------------------------------------------------+                                                                                   
# | Resultado: 1 T                                                |
# +---------------------------------------------------------------+
#

# Dicionário com os valores decimais correspondentes a cada prefixo
prefixos = {
    'k': 10**3,
    'M': 10**6,
    'G': 10**9,
    'T': 10**12
}

# Entrada de dados
valor = float(input("Digite o valor: "))
prefixo_inicial = input("Digite o prefixo inicial (k, M, G, T): ").strip()
prefixo_desejado = input("Digite o prefixo que deseja visualizar (k, M, G, T): ").strip()

# Verifica se os prefixos digitados são válidos
if prefixo_inicial not in prefixos or prefixo_desejado not in prefixos:
    print("Prefixo inválido!")
else:
    # Converte o valor para a unidade base (sem prefixo)
    valor_base = valor * prefixos[prefixo_inicial]
    
    # Converte o valor da unidade base para o prefixo desejado
    valor_convertido = valor_base / prefixos[prefixo_desejado]

    # Exibe o resultado
    print(f"Resultado: {valor_convertido:.3f} {prefixo_desejado}")


