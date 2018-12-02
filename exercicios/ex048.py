soma = 0
contador = 0
for n in range(1,501 ,2):
	if(n % 3 == 0):
		soma += n
		contador += 1

print("A soma foi {} com {} numeros".format(soma,contador))
