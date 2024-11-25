# Função para calcular a associação em série dos resistores
def calcular_associacao_serie():
    while True:
        # Solicita os valores dos resistores
        R1 = float(input("Digite o valor de R1 (ou 0 para sair): "))
        if R1 == 0:
            break
        
        R2 = float(input("Digite o valor de R2 (ou 0 para sair): "))
        if R2 == 0:
            break
        
        R3 = float(input("Digite o valor de R3 (ou 0 para sair): "))
        if R3 == 0:
            break
        
        # Calcula o valor da associação em série
        R = R1 + R2 + R3
        print(f"O valor da associação em série dos resistores é: {R:.2f} Ohms\n")

# Chama a função para executar o cálculo
calcular_associacao_serie()
