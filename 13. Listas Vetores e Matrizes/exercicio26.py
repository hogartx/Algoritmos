# Função para calcular a associação em paralelo dos resistores
def calcular_associacao_paralelo():
    while True:
        # Solicita os valores dos resistores
        R1 = float(input("Digite o valor de R1 (ou 0 para sair): "))
        if R1 == 0:
            break
        
        R2 = float(input("Digite o valor de R2 (ou 0 para sair): "))
        if R2 == 0:
            break
        
        # Verifica se os valores são positivos
        if R1 <= 0 or R2 <= 0:
            print("Os valores dos resistores devem ser positivos. Tente novamente.")
            continue
        
        # Calcula o valor da associação em paralelo
        R = (R1 * R2) / (R1 + R2)
        print(f"O valor da associação em paralelo dos resistores é: {R:.2f} Ohms\n")

# Chama a função para executar o cálculo
calcular_associacao_paralelo()
