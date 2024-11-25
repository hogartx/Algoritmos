# Função para realizar a conversão de Celsius para Fahrenheit
def conversao_celsius_para_fahrenheit():
    print("Temperatura em Celsius | Temperatura em Fahrenheit")
    # Laço que percorre de 0 até 100°C, com incremento de 10
    for celsius in range(0, 101, 10):
        fahrenheit = celsius * 1.8 + 32
        print(f"{celsius}°C              | {fahrenheit:.2f}°F")

# Chama a função para executar a conversão
conversao_celsius_para_fahrenheit()
