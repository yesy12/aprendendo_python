from random import randint

def sorteia(lista):
	print("\033[35mNumeros sorteados foram \033[m",end="")	
	while len(lista) < 6:
		numeros = randint(1,100)
		print(f"\033[34m{numeros} \033[m",end="")
		lista.append(numeros)
	print()
	
def somaPar(lista):
	soma = 0
	print("\033[35mOs números somados são \033[m",end="")
	for n in lista:
		if(n % 2 == 0):	
			soma += n
			print(f"\033[32m{n} \033[m",end="")
	print(f"\n\033[35mO valor da soma é \033[32m{soma}\033[m")
	
numeros = []
sorteia(numeros)
somaPar(numeros)