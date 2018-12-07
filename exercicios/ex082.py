numeros = []
pares = []
impares = []

while True:
	num = int(input("Digite um numero: ").strip())
	numeros.append(num)
	
	if(num % 2 == 0):
		pares.append(num)
	elif(num % 2 == 1):
		impares.append(num)
	
	cont = input("Deseja continuar[s/n]? ").strip().upper()
	if(cont == "N"):
		break


print(f"A lista de numeros são ({numeros})")
print(f"A lista de numeros pares são ({pares})") 
print(f"A lista de numeros impares são ({impares})")
