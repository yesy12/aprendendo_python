print("Descobrir se faz triangulo")
r1=int(input("Digite um valor de segmento: ").strip())
r2=int(input("Digite outro valor de segmento: ").strip())
r3=int(input("Digite o último valor de segmento: ").strip())

if(r1 < (r2 +r3) and r2 < (r3+r1) and r3 < (r1+r2) ):
	print("Os segmentos {},{} e {} podem formar triangulo".format(r1,r2,r3))
else:
	print("Não podem formar triangulo")
