#9) A potência (P) consumida por determinado aparelho eletroeletrônico é definida pela tensão (V) multiplicada pela corrente (A). Elaborar um programa que, a partir da tensão e corrente fornecidas pelo usuário, calcule e mostre na tela a potência.

# Solicita a tensão (V) e a corrente elétrica (A) do usuário
V = float(input("Digite a tensão (V) em volts: "))
A = float(input("Digite a corrente elétrica (A) em amperes: "))

# Calcula a potência usando a fórmula (P = V * A)
P = V * A

# Exibe o valor da potência
print(f"A potência consumida pelo aparelho é de {P} watts")
