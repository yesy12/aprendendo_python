print("Aproveitamento dos Jogadores")

jogadores = {}
total = 0
indice = 0

while True:
	nome = input("Digite o nome: ")

	partidas = int(input("Digite o numero de partida: "))
	golsPartidas = []
	
	for partida in range(1,partidas+1):
		gols = int(input(f"Digite os gols da partida {partida}: ").strip())	
		total += gols
		golsPartidas.append(gols)	
	
	jogadores[indice] = {
		"nome":nome,
		"gols":golsPartidas[:],
		"total":total
	}
	
	total = 0
	indice += 1
	golsPartidas.clear()
	
	cont = input("Você quer continuar? [s/n]: ").upper().strip()
	
	if(cont == "N"):
		break
		
print("\nINDICE NOME GOLS TOTAL")		
for key,value in jogadores.items():
	print(key,end="")
	for keyDado,keyValue in value.items():
		print(f" {keyValue} ",end="")
	print()

while True:
	print("\nInformações sobre Jogadores")
	valorIndice = int(input("Números e 999 para cancelar: "))

	if(valorIndice == 999):
		break
	else:
		if(valorIndice >= 0 and valorIndice < len(jogadores)):
			print(f"\nO jogador {jogadores[valorIndice]['nome']}")
			for pos,gol in enumerate(jogadores[valorIndice]['gols']):
				print(f"Na partida {pos+1} teve {gol} gols")
		else:
			print(f"{valorIndice} fora de Indice")