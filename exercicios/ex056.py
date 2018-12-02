media = 0
mulherMenos20 = 0
maisVelho = 0
nomeHomem = ""

for n in range(0,4):
	nome = input("\nDigite seu nome ({}/4): ".format(n+1)).strip()
	idade = int(input("Digite sua idade ({}/4): ".format(n+1)).strip())
	sexo = input("Digite seu sexo ({}/4): ".format(n+1)).upper().strip()

	if( (maisVelho == 0 or maisVelho < idade) and sexo == "M"):
		maisVelho = idade
		nomeHomem = nome
	if(sexo == "F" and idade < 20):
		mulherMenos20 += 1

	media +=idade


media/=4

print("\nA media de idade é {}".format(media))
print("O nome do Homem mais velho é {} com {} anos".format(nomeHomem,maisVelho))
print("Existem {} mulheres com menos de 20 anos".format(mulherMenos20))
