pessoas = {}
mulheres = {}
acimaIdade = {}
dados = []
pessoa = 0
media = 0

while True:
	nome = input("Digite seu nome: ").strip()
	sexo = input("Digite seu sexo: ").strip().upper()
	idade = int(input("Digite sua idade: ").strip())
	
	dados.append(nome)
	dados.append(sexo)
	dados.append(idade)
	
	cont = input("Deseja continuar ?[s/n]: ").upper().strip()	
	pessoa +=1
	
	pessoas[f"pessoa{pessoa}"] = dados[:] 
	dados.clear()
	
	if(cont == "N"):
		break	

print(f"Quantidade de pessoas é {len(pessoas)}")

for key,value in pessoas.items():
	for pos,dado in enumerate(value):
		if(pos == 1 and dado == "F"):
			mulheres[key] = value[0]
		if(pos == 2):
			media += (dado / len(pessoas))
	
print(f"A média de idade é {media:.2f} anos")
print(f"A lista com Mulheres é {mulheres}")

for key,value in pessoas.items():
	if(value[2] > media):
		acimaIdade[key] = value[0]

print(f"A lista com pessoas acima da média é {acimaIdade}")