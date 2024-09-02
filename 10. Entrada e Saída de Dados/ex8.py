#8) Adotando como referência o exercício 7, calcule e exiba a intensidade da corrente elétrica (A) a partir da tensão (V) e resistência (R) que o usuário irá fornecer ao programa.

# Solicita a tensão (V) e a resistência (R) do usuário
V = float(input("Digite a tensão (V) aplicada: "))
R = float(input("Digite a resistência (R) do condutor: "))

# Calcula a intensidade da corrente usando a fórmula (A = V / R)
R = V / R

# Exibe o valor da corrente elétrica
print(f"A intensidade da corrente elétrica é: {R} amperes")
