# 1) Criar um programa que receba quatro números inteiros e exiba o menor deles.


# Solicita quatro números inteiros do usuário

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))
valor3 = int(input("Digite o terceiro número: "))
valor4 = int(input("Digite o quarto número: "))

# Verifica qual valor é o menor

if (valor1 < valor2) and (valor1 < valor3) and (valor1 < valor4):
 print ("O menor é: ", valor1)
elif (valor2 < valor3) and (valor2 < valor4):
 print ("O menor é: ", valor2)
elif (valor3 < valor4):
 print ("O menor é: ", valor3)
else:
 print ("O menor é: ", valor4)

# Breve explicação sobre if, elif e else

# if: Verifica a primeira condição. Se for verdadeira, o bloco de código correspondente é executado, e o restante da estrutura é ignorado.

# elif: "Else if" permite verificar várias condições adicionais se a condição do if não for verdadeira. Você pode ter quantos elif forem necessários para cobrir todas as condições possíveis.

# else: Opcionalmente, captura todos os casos que não foram tratados pelas funções if e elif.


