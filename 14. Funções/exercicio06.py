# Funções de conversão
def celsius_para_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit + 459.67) / 1.8

def kelvin_para_fahrenheit(kelvin):
    return (kelvin * 1.8) - 459.67

# Função para realizar a conversão
def realizar_conversao():
    while True:
        # Solicita o tipo de conversão
        print("\nEscolha a conversão:")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Celsius para Kelvin")
        print("4. Kelvin para Celsius")
        print("5. Fahrenheit para Kelvin")
        print("6. Kelvin para Fahrenheit")
        opcao = int(input("Digite o número da conversão: "))

        # Solicita a temperatura
        temperatura = float(input("Digite a temperatura para conversão: "))

        # Realiza a conversão com base na opção escolhida
        if opcao == 1:
            resultado = celsius_para_fahrenheit(temperatura)
            print(f"{temperatura}° Celsius equivale a {resultado}° Fahrenheit.")
        elif opcao == 2:
            resultado = fahrenheit_para_celsius(temperatura)
            print(f"{temperatura}° Fahrenheit equivale a {resultado}° Celsius.")
        elif opcao == 3:
            resultado = celsius_para_kelvin(temperatura)
            print(f"{temperatura}° Celsius equivale a {resultado} Kelvin.")
        elif opcao == 4:
            resultado = kelvin_para_celsius(temperatura)
            print(f"{temperatura} Kelvin equivale a {resultado}° Celsius.")
        elif opcao == 5:
            resultado = fahrenheit_para_kelvin(temperatura)
            print(f"{temperatura}° Fahrenheit equivale a {resultado} Kelvin.")
        elif opcao == 6:
            resultado = kelvin_para_fahrenheit(temperatura)
            print(f"{temperatura} Kelvin equivale a {resultado}° Fahrenheit.")
        else:
            print("Opção inválida. Tente novamente.")
            continue

        # Pergunta se o usuário deseja realizar outra conversão
        nova_conversao = input("\nDeseja realizar outra conversão? (sim/não): ").strip().lower()
        if nova_conversao != 'sim':
            print("Encerrando o programa...")
            break

# Chama a função principal
realizar_conversao()
