maiores = 0
menores = 0
anoAtual = 2018

for n in range(0,7):
	ano = int(input("Digite o ano de nascimento ({}/7): ".format(n+1)).strip())

	if( (anoAtual - ano) >= 18):
		maiores += 1

	elif( (anoAtual - ano) < 18):
		menores += 1

print("Existem pessoas {} de menores".format(menores))
print("Existem pessoas {} de maiores".format(maiores))
