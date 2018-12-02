from random import randint

num = randint(0,5)

valor = int(input("Digite um numero: ").strip())

if(num == valor):
	print("Você ganhou!")
else:
	print("Você perdeu!")
