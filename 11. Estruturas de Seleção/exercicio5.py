# 5) Dividir dois números reais, digitados pelo usuário, e exibir apenas a parte inteira do resultado, ou seja, desprezar as casas decimais. 

# Entrada dos números reais
numero1 = float(input("Digite o primeiro número real: "))
numero2 = float(input("Digite o segundo número real: "))

# Divisão
resultado = numero1 / numero2

# Exibindo apenas a parte inteira do resultado
parte_inteira = int(resultado)
print(f"A parte inteira da divisão de {numero1} por {numero2} é: {parte_inteira}")
