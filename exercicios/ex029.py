vel=int(input("Digite sua velocidade: ").strip())

if(vel>80):
	preco=(vel-80)*7
	print("Você foi multado em R$ {}".format(preco))
