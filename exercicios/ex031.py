dist =int(input("Digite a sua distancia: ").strip())

if(dist <200):
	preco=0.5*dist
else:
	preco=0.45*dist

preco=str(preco).replace(".",",")

print("Seu custo para {} kms é de R$ {}".format(dist,preco))
