import random

# Função para adivinhar o número mágico
def adivinhar_numero_magico():
    # Sorteia o número mágico entre 0 e 500
    numero_magico = random.randint(0, 500)
    
    tentativas = 0  # Contador de tentativas

    print("Bem-vindo ao jogo! Tente adivinhar o número mágico entre 0 e 500.")

    # Loop que continua até o usuário acertar o número mágico
    while True:
        # Solicita ao usuário uma tentativa
        tentativa = int(input("Qual é o seu palpite? "))
        tentativas += 1  # Incrementa o número de tentativas

        # Verifica se o palpite é maior, menor ou igual ao número mágico
        if tentativa < numero_magico:
            print("O número mágico é maior! Tente novamente.")
        elif tentativa > numero_magico:
            print("O número mágico é menor! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número mágico {numero_magico}!")
            break  # Sai do loop quando o usuário acerta

    # Classificação com base no número de tentativas
    if tentativas <= 3:
        print("Você foi muito sortudo!")
    elif tentativas <= 6:
        print("Você foi sortudo!")
    elif tentativas <= 10:
        print("Você é normal.")
    else:
        print("Tente novamente!")

# Chama a função para iniciar o jogo
adivinhar_numero_magico()
