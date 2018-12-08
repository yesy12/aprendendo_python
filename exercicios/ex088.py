from random import randint

megasena = []
listaNumeros = []
print("MegaSena")
cartelas = int(input("Digite o número de cartelas: ").strip())

for numeros in range(0,cartelas):
	while True:
		numero = randint(1,60)
		
		if( not(numero in listaNumeros) ):
			listaNumeros.append(numero)
		if(len(listaNumeros) ==6):
			break
			
	listaNumeros.sort()
	megasena.append(listaNumeros[:])
	listaNumeros = []

for cartela in megasena:
	print(cartela)