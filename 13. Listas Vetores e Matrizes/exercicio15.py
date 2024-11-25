# Função para calcular o fatorial de um número
def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

# Solicita o número inteiro ao usuário
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Verifica se o número é negativo (fatorial de números negativos não existe)
if numero < 0:
    print("Fatorial de número negativo não existe.")
else:
    # Calcula e exibe o fatorial
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}.")
