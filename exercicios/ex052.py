print("Verificando se é primo")
numero = int(input("Digite um numero: "))

tentativa = 0
print("\n")

for n in range(1,numero+1):
	if(numero % n ==0):
		tentativa+=1
		print("\033[33m{} divisivel por {}\033[m".format(numero,n))



if(tentativa > 2):
	print("\n\033[31m{} não é primo\033[m\n".format(numero))
elif(tentativa ==2):
	print("\n\033[4;32m{} é primo\033[m\n".format(numero))
