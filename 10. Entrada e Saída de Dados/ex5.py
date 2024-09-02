#5) Uma determinada loja precisa calcular o preço de venda de um produto. O cálculo deverá ser efetuado através da multiplicação do preço unitário pela quantidade vendida e, posteriormente, subtrair o valor do desconto. Considerar todas as variáveis do tipo de dado real e que as mesmas serão digitadas pelo usuário.

# Solicita o preço unitário, a quantidade vendida e o desconto
# Como no enunciado diz ser "valor" do desconto consideramos em R$ e não em porcentagem, pois faria toda diferença no código.
# Atenção ao int e float nas variáveis, colocamos int na quantidade pois não venderiamos meio produto nesse caso e float nas outras duas pois o valor não necessariamente precisará ser inteiro.
preco_unitario = float(input("Digite o preço unitário do produto em R$: "))
quantidade = int(input("Digite a quantidade vendida: "))
desconto = float(input("Digite o valor do desconto em R$: "))

# Calcula o preço de venda
preco_venda = (preco_unitario * quantidade) - desconto

# Exibe o preço final de venda
print(f"O preço final de venda é: R${preco_venda}")