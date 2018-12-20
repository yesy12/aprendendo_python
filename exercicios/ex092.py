from datetime import date
hj = date.today()
pessoa = {}
pessoa["nome"] = input("Digite o nome da pessoa: ").strip()

while True:
	pessoa["nascimento"] = int(input("Digite o ano de nascimento: "))
	if(pessoa["nascimento"] <= hj.year):
		break
	
pessoa["idade"] = hj.year - pessoa["nascimento"]

pessoa["ctps"] = int(input("Digite a Carteira de Trabalho e 0 se não tem: "))

if(pessoa["ctps"] != 0 and pessoa["idade"] > 14):
	while True:
		pessoa["contratacao"] = int(input("Digite o ano de Contratação: "))
		if( not(pessoa["contratacao"] <= pessoa["nascimento"])):
			break
			
	pessoa["salario"] = int(input("Digite o seu salário:R$ "))
	pessoa["trabalhando"] = (hj.year - pessoa["contratacao"])
	pessoa["restando"] = 35 - pessoa["trabalhando"]
	pessoa["aposentadoria"] = pessoa["idade"] + pessoa["restando"]
	
	del(pessoa["trabalhando"])
	del(pessoa["restando"])
del(pessoa["nascimento"])
	
	
print("\nValores \n")
for key,value in pessoa.items():
	print(f"{key} tem o valor {value}")