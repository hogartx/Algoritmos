# Função para somar
def somar(valor1, valor2):
    return valor1 + valor2

# Função para subtrair
def subtrair(valor1, valor2):
    return valor1 - valor2

# Função para multiplicar
def multiplicar(valor1, valor2):
    return valor1 * valor2

# Função para dividir
def dividir(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "Erro: Divisão por zero não permitida."

# Função principal
def calculadora():
    print("Calculadora Simples")
    
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    
    # Chama as funções e recebe o valor retornado
    resultado_soma = somar(valor1, valor2)
    resultado_subtracao = subtrair(valor1, valor2)
    resultado_multiplicacao = multiplicar(valor1, valor2)
    resultado_divisao = dividir(valor1, valor2)
    
    # Exibe os resultados
    print(f"Soma: {resultado_soma}")
    print(f"Subtração: {resultado_subtracao}")
    print(f"Multiplicação: {resultado_multiplicacao}")
    print(f"Divisão: {resultado_divisao}")

# Chama a função principal
calculadora()
