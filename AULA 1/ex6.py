#6) Calcular a média final de um aluno considerando que o mesmo irá realizar duas provas (P1 e P2), sendo que a P1 deverá ter peso 4 e a P2 peso 6. Adotar que as notas são do tipo de dado real e que elas serão fornecidas pelo usuário.

# Solicita as notas das provas P1 e P2
p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))

# Calcula a média ponderada (P1 com peso 4 e P2 com peso 6)
# A prova P1 tem peso 4 (ou seja, ela conta como 40% da nota final).
# A prova P2 tem peso 6 (ou seja, ela conta como 60% da nota final).
# Multiplicamos a nota da P1 por seu peso, ou seja, P1 × 4.
# Multiplicamos a nota da P2 por seu peso, ou seja, P2 × 6.
# Somamos os resultados das multiplicações: (P1 × 4) + (P2 × 6).
# Para obter a média final, dividimos o valor total obtido pela soma dos pesos. No caso, a soma dos pesos é 10, pois 4 (de P1) + 6 (de P2) = 10.

media_final = (p1 * 4 + p2 * 6) / 10

# Exibe a média final
print(f"A média final do aluno é: {media_final}")
