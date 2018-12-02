valor = 0
tentativa = 0
media = 0

maior = 0
menor = 0

print("\033[4;31mDigite 999\033[m")

while valor != 999:
	valor = int(input("Digite um numero: "))
	if( tentativa == 0):
		maior = valor
		menor = valor
	if( valor > maior and valor != 999):
		maior = valor
	if( valor < menor and valor != 999):
		menor = valor
	cont = input("Você quer continuar?: ").strip().upper()
	if( cont == "N"):
		valor = 999

	tentativa += 1
	media += valor

media /= tentativa

print("A média deu {} com {} tentativas".format(media,tentativa))
print("O maior numero é {}".format(maior))
print("O menor numero é {}".format(menor))
