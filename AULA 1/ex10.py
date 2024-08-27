#10) Considerando o exercício 9 calcule e exiba a corrente (A) que circula por determinado aparelho eletroeletrônico a partir da potência (P) e tensão (V) digitadas pelo usuário.

# Solicita a potência (P) e a tensão (V) do usuário
P = float(input("Digite a potência (P) consumida em watts: "))
V = float(input("Digite a tensão (V) aplicada em volts: "))

# Calcula a corrente usando a fórmula (A = P / V)
A = P / V

# Exibe o valor da corrente elétrica
print(f"A corrente que circula pelo aparelho é de {A} amperes")
