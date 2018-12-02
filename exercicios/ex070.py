totalGasto = produtosMais1000 = produtoMaisBarato = tentativa = 0

nomeProduto = ""

while True:
	tentativa += 1
	nome = input("Digite o nome do produto: ").strip()
	preco = float(input("Digite o preço:R$ ").strip().upper())

	totalGasto += preco
	if(tentativa == 1):
		produtoMaisBarato = preco
		nomeProduto = nome
	if(produtoMaisBarato > preco):
		produtoMaisBarato = preco
		nomeProduto = nome
	if(preco >= 1000):
		produtosMais1000 += 1

	while True:
		continuar = input("Deseja continuar?:[S/N] ").strip().upper()
		if(continuar == "S" or continuar == "N"):
			break

	if(continuar == "N"):
		break


print(f"Total Gasto foi R$ {totalGasto:.2f}")
print(f"O produto mais barato é {nomeProduto} custando R$ {produtoMaisBarato:.2f}")
print(f"Existem {produtosMais1000} que custam R$ 1000 ou mais")
