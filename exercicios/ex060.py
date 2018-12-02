print("Fatorial")
fat = int(input("Digite um numero: "))
fatRes = fat
valor = 1

while fat != 1:
	valor *= fat
	fat -= 1

print("o {} em fatorial é {}".format(fatRes,valor))
