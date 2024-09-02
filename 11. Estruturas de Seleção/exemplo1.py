#
#
#
#
#
#

import time
nome = input("Digite o seu nome: ")
anoNasc = int(input("Digite o ano de nascimento: "))
anoAtual = int(time.strftime("%Y"))
idade = anoAtual - anoNasc
maioridade = ""
if idade >= 18:
 maioridade = "maior"
else:
 maioridade = "menor"
print (nome, ", a sua idade é", idade, "anos e você é",
maioridade, "de idade")
