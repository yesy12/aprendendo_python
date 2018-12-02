from random import randint
print("""1 para Papel
\n2 para Pedra
\n3 para Tesoura
""")
jog = int(input("Digite um numero: ").strip())

valorPc= randint(1,3)

if(valorPc == 1):
	escolhaPc = "Papel"
elif(valorPc == 2):
	escolhaPc = "Pedra"
elif(valorPc == 3):
	escolhaPc = "Tesoura"

if(jog == 1):
	escolhaJog = "Papel"
elif(jog == 2):
	escolhaJog = "Pedra"
elif(jog == 3):
	escolhaJog = "Tesoura"

print("Você jogou {}".format(escolhaJog))
print("O PC jogou {}\n".format(escolhaPc))

if(escolhaPc == "Papel" and  escolhaJog == "Pedra"):
	print("O pc ganhou de você")
elif(escolhaPc == "Pedra" and escolhaJog == "Tesoura"):
	print("O pc ganhou de você")
elif(escolhaPc == "Tesoura" and escolhaJog == "Papel"):
	print("O pc ganhou de você")
elif(escolhaPc == escolhaJog):
	print("Empatou")
else:
	print("Você ganhou do PC")
