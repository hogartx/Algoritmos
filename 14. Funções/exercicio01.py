# Função para somar
def somar(valor1, valor2):
    resultado = valor1 + valor2
    print("Soma: ", resultado)

# Função para subtrair
def subtrair(valor1, valor2):
    resultado = valor1 - valor2
    print("Subtração: ", resultado)

# Função para multiplicar
def multiplicar(valor1, valor2):
    resultado = valor1 * valor2
    print("Multiplicação: ", resultado)

# Função para dividir
def dividir(valor1, valor2):
    if valor2 != 0:
        resultado = valor1 / valor2
        print("Divisão: ", resultado)
    else:
        print("Erro: Divisão por zero não permitida.")

# Função principal
def calculadora():
    print("Calculadora Simples")
    
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    
    # Chama as funções para realizar as operações
    somar(valor1, valor2)
    subtrair(valor1, valor2)
    multiplicar(valor1, valor2)
    dividir(valor1, valor2)

# Chama a função principal
calculadora()
