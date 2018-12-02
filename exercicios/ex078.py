lista = []
for a in range(1,6):
	n = int(input(f"Digite um número ({a}/5): "))
	lista.append(n)
	
print(f"Menor valor é {min(lista)} na posição {lista.index(min(lista))}°")
print(f"Maior valor é {max(lista)} na posição {lista.index(max(lista))}°")