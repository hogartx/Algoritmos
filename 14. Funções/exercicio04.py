# Função que retorna o maior valor de uma lista de números reais (sem usar max())
def maior_valor(lista):
    maior = lista[0]  # Assume que o primeiro valor é o maior
    for numero in lista:
        if numero > maior:
            maior = numero  # Atualiza o maior valor
    return maior

# Exemplo de uso
numeros = [2.5, 4.3, 7.8, 1.2, 9.0, 3.5]

# Chama a função e exibe o maior valor
resultado = maior_valor(numeros)
print(f"O maior valor da lista é: {resultado}")
