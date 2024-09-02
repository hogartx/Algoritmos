# Breve explicação sobre if, elif e else

# if: Verifica a primeira condição. Se for verdadeira, o bloco de código correspondente é executado, e o restante da estrutura é ignorado.

# elif: "Else if" permite verificar várias condições adicionais se a condição do if não for verdadeira. Você pode ter quantos elif forem necessários para cobrir todas as condições possíveis.

# else: Opcionalmente, captura todos os casos que não foram tratados pelas funções if e elif.


# Solicita a nota do usuário
nota = float(input("Digite a nota do aluno: "))

# Verifica a nota e classifica o aluno
if nota >= 90:
    print("Aprovado com Distinção")
elif nota >= 80:
    print("Aprovado com Mérito")
elif nota >= 70:
    print("Aprovado")
elif nota >= 60:
    print("Aprovado Condicional")
else:
    print("Reprovado")

