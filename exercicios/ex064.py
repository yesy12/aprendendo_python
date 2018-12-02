valor = 0
tentativa = 0
soma = 0

print("\033[4;31mDigite 999\033[m")

while valor != 999:
	valor = int(input("Digite um numero: "))
	if( valor != 999):
		tentativa += 1
		soma += valor

print("A soma deu {} com {} tentativas".format(soma,tentativa))


