# 6) Considerando que a aprovação de um aluno em determinada disciplina requer uma média final maior ou igual a 6,0 (seis). Elaborar um programa que receba duas notas, realize o calculo da média, exiba o valor calculado e também se o aluno está aprovado ou reprovado.

# Solicita as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média das duas notas
media = (nota1 + nota2) / 2



# if media >= 6.0:: Verifica se a média é maior ou igual a 6.0.

# Se verdadeiro, print("O aluno está aprovado.").

# Caso contrário, print("O aluno está reprovado.").

# Verifica se o aluno está aprovado ou reprovado
if media >= 6.0:
    print(f"A média final é {media}, e o aluno está APROVADO.")
else:
    print(f"A média final é {media}, e o aluno está REPROVADO.")
