# Função para converter um intervalo de tempo em segundos
def converter_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

# Solicita o primeiro intervalo de tempo
print("Digite o primeiro intervalo de tempo:")
horas1 = int(input("Horas: "))
minutos1 = int(input("Minutos: "))
segundos1 = int(input("Segundos: "))

# Solicita o segundo intervalo de tempo
print("\nDigite o segundo intervalo de tempo:")
horas2 = int(input("Horas: "))
minutos2 = int(input("Minutos: "))
segundos2 = int(input("Segundos: "))

# Converte ambos os intervalos para segundos
tempo1_segundos = converter_para_segundos(horas1, minutos1, segundos1)
tempo2_segundos = converter_para_segundos(horas2, minutos2, segundos2)

# Calcula a diferença de tempo em segundos
diferenca_segundos = abs(tempo1_segundos - tempo2_segundos)

# Converte a diferença de volta para horas, minutos e segundos
horas_diff = diferenca_segundos // 3600
minutos_diff = (diferenca_segundos % 3600) // 60
segundos_diff = diferenca_segundos % 60

# Exibe a diferença de tempo
print(f"\nA diferença de tempo é: {horas_diff} horas, {minutos_diff} minutos e {segundos_diff} segundos.")
