lista = []

while True:
	valor = int(input("Digite um número: ").strip ())
	lista.append(valor)
	
	cont = input("Deseja continuar?[s/n] ").strip().upper()
	if(cont == "N"):
		break
	
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} numeros")
print(f"A ordem decrescente é {lista}")
if(5 in lista):
	print("Existe 5 nessa lista")
else:
	print("Não Existe 5 nessa lista")