import random

# Inicializando contadores
caras = 0
coroas = 0

# Simulando 10 lançamentos da moeda
for _ in range(10):
    resultado = random.choice(["cara", "coroa"])  # Escolhe aleatoriamente entre "cara" e "coroa"
    if resultado == "cara":
        caras += 1
    else:
        coroas += 1

# Exibindo os resultados
print(f"Resultado dos lançamentos:")
print(f"Caras: {caras}")
print(f"Coroas: {coroas}")
