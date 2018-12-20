print("Aproveitamento dos Jogadores")

jogador = {}
qtdGols = []
total = 0

jogador["nome"] = input("Digite o nome do Jogador: ")
qtdPartidas = int(input("Digite a quantidade de partidas: "))

for gols in range(1,qtdPartidas+1):
	golsJog = int(input(f"Quantidade de Gols da partida {gols} feito por {jogador['nome']}: "))
	total += golsJog
	qtdGols.append(golsJog)

jogador["gols"] = qtdGols[:]
jogador["total"] = total
	
for key,value in jogador.items():
	print(f"{key} tem resultado de {value}")
	
print(f"O jogador {jogador['nome']} nas {len(jogador['gols'])} partidas")

for pos,value in enumerate(jogador["gols"]):
	print(f" fez {value} gols na partida {pos+1}")
print(f"Totalizando {jogador['total']} gols")