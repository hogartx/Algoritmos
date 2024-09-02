# 9) Através do cálculo do Índice de Massa Corporal (IMC) é possível saber se uma pessoa está acima ou abaixo dos parâmetros ideais de peso em relação a sua altura. Para calcular o IMC é necessário dividir o peso (Kg) de Lógica de Programação e Algoritmos em Python Prof. Cláudio Luís V. Oliveira 44 uma pessoa pela sua altura (m) elevada ao quadrado. Elaborar um programa que exiba o valor do IMC de uma pessoa e mostre a sua situação em relação à tabela a seguir:
# +----------------------+--------------------------------------------+
# | VALOR DO IMC         | SITUAÇÃO                                  |
# +----------------------+--------------------------------------------+
# | Abaixo de 18,5       | Você está abaixo do peso ideal             |
# +----------------------+--------------------------------------------+
# | Entre 18,5 e 24,9    | Parabéns, você está em seu peso normal!    |
# +----------------------+--------------------------------------------+
# | Entre 25,0 e 29,9    | Você está acima de seu peso (sobrepeso)    |
# +----------------------+--------------------------------------------+
# | Entre 30,0 e 34,9    | Obesidade grau I                          |
# +----------------------+--------------------------------------------+
# | Entre 35,0 e 39,9    | Obesidade grau II                         |
# +----------------------+--------------------------------------------+
# | 40,0 e acima         | Obesidade grau III                        |
# +----------------------+--------------------------------------------+

# Solicita o peso e a altura do usuário
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o valor do IMC
print(f"O seu IMC é: {imc:.1f}")

# Determina e exibe a situação com base no IMC
if imc < 18.5:
    situacao = "Você está abaixo do peso ideal"
elif 18.5 <= imc < 25.0:
    situacao = "Parabéns, você está em seu peso normal!"
elif 25.0 <= imc < 30.0:
    situacao = "Você está acima de seu peso (sobrepeso)"
elif 30.0 <= imc < 35.0:
    situacao = "Obesidade grau I"
elif 35.0 <= imc < 40.0:
    situacao = "Obesidade grau II"
else:
    situacao = "Obesidade grau III"

print(situacao)
