# Funções de conversão
def celsius_para_fahrenheit(celsius):
    return celsius * 1.8 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit + 459.67) / 1.8

def kelvin_para_fahrenheit(kelvin):
    return kelvin * 1.8 - 459.67

# Função principal
def realizar_conversao():
    while True:
        # Solicita ao usuário a temperatura e a opção de conversão
        temperatura = float(input("Digite a temperatura: "))
        print("\nEscolha a conversão:")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Celsius para Kelvin")
        print("4. Kelvin para Celsius")
        print("5. Fahrenheit para Kelvin")
        print("6. Kelvin para Fahrenheit")
        
        opcao = int(input("Digite o número da opção desejada: "))
        
        # Realiza a conversão com base na opção escolhida
        if opcao == 1:
            resultado = celsius_para_fahrenheit(temperatura)
            print(f"{temperatura}°C é igual a {resultado:.2f}°F")
        elif opcao == 2:
            resultado = fahrenheit_para_celsius(temperatura)
            print(f"{temperatura}°F é igual a {resultado:.2f}°C")
        elif opcao == 3:
            resultado = celsius_para_kelvin(temperatura)
            print(f"{temperatura}°C é igual a {resultado:.2f}K")
        elif opcao == 4:
            resultado = kelvin_para_celsius(temperatura)
            print(f"{temperatura}K é igual a {resultado:.2f}°C")
        elif opcao == 5:
            resultado = fahrenheit_para_kelvin(temperatura)
            print(f"{temperatura}°F é igual a {resultado:.2f}K")
        elif opcao == 6:
            resultado = kelvin_para_fahrenheit(temperatura)
            print(f"{temperatura}K é igual a {resultado:.2f}°F")
        else:
            print("Opção inválida. Tente novamente.")
            continue
        
        # Pergunta se o usuário deseja realizar uma nova conversão
        nova_conversao = input("\nDeseja realizar uma nova conversão? (sim/não): ").strip().lower()
        if nova_conversao != "sim":
            print("Programa encerrado.")
            break

# Executa a função principal
realizar_conversao()
