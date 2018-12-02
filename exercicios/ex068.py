print("Par ou impar")

from random import randint 

acertos = 0

while True:
	escolhaJog = input("Digite sua escolha: ").strip().upper()

	numeroAleatorio = randint(0,1000)
	print(f"O numero foi {numeroAleatorio}")
	if(numeroAleatorio % 2 == 0):
		if(escolhaJog == "PAR"):
			acertos += 1
		elif(escolhaJog == "IMPAR"):
			break

	elif(numeroAleatorio % 2 == 1):
		if(escolhaJog == "IMPAR"):
			acertos += 1
		elif(escolhaJog == "PAR"):
			break


print(f"Você ganhou {acertos}")
