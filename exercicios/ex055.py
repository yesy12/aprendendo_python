maior = 0
menor = 0

for n in range(1,6):
	peso = float(input("Digite um peso ({}/5): ".format(n)))
	if(n == 1):
		maior = peso
		menor = peso
	elif(peso > maior):
		maior = peso
	elif(peso < menor ):
		menor = peso

print("O menor peso foi {} kgs".format(menor))
print("O maior peso foi {} kgs".format(maior))
