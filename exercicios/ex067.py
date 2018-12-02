print("TABUADA")
while True:
	valor = int(input("Digite um numero: "))
	if(valor < 0):
		break
	else:
		for a in range(1,11):
			print(f"{a} x {valor} = {a*valor}")
