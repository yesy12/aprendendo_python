def dobra(lista):
	for pos,valor in enumerate(lista):
		lista[pos] = valor*2
		
lista = [7,2.4,9.3,9.2]
print(lista)

dobra(lista)
print(lista)