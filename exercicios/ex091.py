from random import randint
posicao = 1

jogadores = {
	"jogador1":0,
	"jogador2":0,
	"jogador3":0,
	"jogador4":0
}
print("Valores sorteados")

for key in jogadores.keys():
	valor = randint(1,6)
	jogadores[key] = valor
	print(f"O {key} tirou {valor}")
	
print("Ranking")
jogadores.items().sort()
print(jogadores)