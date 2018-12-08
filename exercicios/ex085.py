numeros = [ [],[] ]

for n in range(1,8):
	numero = int(input(f"Digite um numero ({n}/7): ").strip())
	
	if(numero % 2 == 0):
		numeros[0].append(numero)
	else:
		numeros[1].append(numero)
		
numeros[0].sort()
numeros[1].sort()
print(f"Numeros pares {numeros[0]}")
print(f"Numeros impares {numeros[1]}")