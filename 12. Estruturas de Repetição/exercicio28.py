# 28) A partir do salário e categoria, digitados pelos usuário, calcular o reajuste de salário de determinado funcionário baseando-se na tabela mostrada a seguir, sendo que o programa deverá aceitar tanto letras maiúsculas como minúsculas para determinar a categoria do funcionário. Reajuste Categoria
# +-----------------------------+
# | Reajuste | Categoria        |
# +-----------------------------+
# | 10%      | A, C            |
# | 15%      | B, D, E         |
# | 25%      | F, L            |
# | 35%      | G, H            |
# | 50%      | I, J            |
# +-----------------------------+


# Entrada de dados
salario = float(input("Digite o salário do funcionário: "))
categoria = input("Digite a categoria do funcionário: ").strip().lower()  # Aceita letras maiúsculas e minúsculas

# Inicializando o percentual de reajuste
percentual_reajuste = 0.0

# Determinando o percentual de reajuste com base na categoria
if categoria in ['a', 'c']:
    percentual_reajuste = 0.10  # 10%
elif categoria in ['b', 'd', 'e']:
    percentual_reajuste = 0.15  # 15%
elif categoria in ['f', 'l']:
    percentual_reajuste = 0.25  # 25%
elif categoria in ['g', 'h']:
    percentual_reajuste = 0.35  # 35%
elif categoria in ['i', 'j']:
    percentual_reajuste = 0.50  # 50%
else:
    print("Categoria inválida.")
    exit()  # Encerra o programa se a categoria for inválida

# Cálculo do novo salário
reajuste = salario * percentual_reajuste
novo_salario = salario + reajuste

# Exibindo o resultado
print(f"\n----- RESULTADO -----")
print(f"Salário Original: R$ {salario:.2f}")
print(f"Percentual de Reajuste: {percentual_reajuste * 100:.0f}%")
print(f"Reajuste: R$ {reajuste:.2f}")
print(f"Novo Salário: R$ {novo_salario:.2f}")
