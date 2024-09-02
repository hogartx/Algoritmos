import time
nome = input("Digite o seu nome: ")
anoNasc = int(input("Digite o ano de nascimento: "))
anoAtual = int(time.strftime("%Y"))
idade = anoAtual - anoNasc
print (nome, "a sua idade é", idade, "anos")