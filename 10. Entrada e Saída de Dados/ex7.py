#7) A Lei de Ohm define que a resistência (R) de um condutor é obtida através da divisão da tensão aplicada (V) dividida pela intensidade de corrente elétrica (A). Desta forma, a partir de uma tensão e corrente, digitadas pelo usuário, calcule e mostre o valor da resistência.

# Solicita a tensão (V) e a corrente elétrica (A) do usuário.
V = float(input("Digite a tensão (V) aplicada: "))
A = float(input("Digite a corrente elétrica (A): "))

# Calcula a resistência usando a Lei de Ohm (R = V / A).
R = V / A

# Exibe o valor da resistência
print(f"A resistência do condutor é: {R} ohms")
