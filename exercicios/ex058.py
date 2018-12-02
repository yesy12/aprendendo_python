from random import randint 

escolhaPc = randint(0,10)

tentativas = 0
escolhaJog = 11

while escolhaJog != escolhaPc:
	tentativas += 1
	escolhaPc = randint(1,10)
	escolhaJog = int(input("digite um numero: "))
	
print("Você tentou {} vezes".format(tentativas))
