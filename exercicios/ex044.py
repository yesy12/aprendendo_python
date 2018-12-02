
valor = float(input("Digite o valor:R$ "))

print("""forma de pagamento
1 avista
2 cartao
3 parcelado
""")

forma = int(input("Digite o numero da forma: "))
vezes = 0

if(forma == 1):
	desconto = 0.1
elif(forma == 2):
	desconto = 0.05
elif(forma == 3):
	vezes = int(input("Digite a quantidade de vezes: "))
	if(vezes <= 2):
		desconto = 0
	elif(vezes > 2):
		juros = 0.2


if(vezes <= 2):
	valorNovo = valor-(valor*desconto)
	print("""O preço antigo era R$ {} com desconto fica R$ {} com {:.0f}% de desconto""".format(valor,valorNovo,desconto*100))
elif(vezes > 2):
	valorNovo = valor+(valor*juros)
	parcela = valorNovo/vezes
	print("""O preco antigo era R$ {} com juros de 20% ficou R$ {}	divididos em {} vezes com valor de R$ {:.2f}""".format(valor,valorNovo,vezes,parcela))

