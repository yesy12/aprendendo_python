lista = []
while True:
	n = int(input("Digite um número: ").strip())
	
	if(n in lista):
		print(f"{n} jã existe na lista")
	else:
		lista.append(n)
		
	cont = input("Deseja continuar [s/n]?: ").strip().upper()
		
	if(cont == "S"):
		break
		
		
lista.sort()
print(f"Os valores digitados foram {lista}")