from random import randint
from operator import itemgetter

jogadores = {
	"jogador1":0,
	"jogador2":0,
	"jogador3":0,
	"jogador4":0
}
print("Valores sorteados\n")

for key in jogadores.keys():
	valor = randint(1,6)
	jogadores[key] = valor
	print(f"O {key} tirou {valor}")

ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)

print("\nPosição no Ranking\n")
for posicao,jogador in enumerate(ranking):
	print(f"{posicao+1} lugar",end="")
	print(f" {jogador[0].upper()} tem {jogador[1]} pontos")