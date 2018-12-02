ano = int(input("Digite o ano de nascimento: ").strip())

idade = (2018-ano)

if(idade <= 9):
	classi = "mirim" 
elif(idade > 9 and idade <= 14):
	classi = "infantil"
elif(idade > 14 and idade <=19):
	classi = "junior"
elif(idade > 19 and idade <=20):
	classi = "senior"
elif(idade >20):
	classi = "master"

print("Sua classificação é {}".format(classi))
