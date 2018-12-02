homemCad = pessoasMais18 = mulheres20 = cont = 0
continuar = "S"
while True:
	idade = int(input("Digite sua idade: ").strip())
	while True:
		sexo = input("Digite seu sexo [M/F]: ").strip().upper()
		if(sexo == "M" or sexo == "F"):
			break
	if(cont > 0):
		while True:
			continuar = input("Você ainda quer continuar?[S/N]: ").strip().upper()
			if(continuar == "S" or continuar == "N"):
				break
	cont += 1

	if(sexo == "M"):
		homemCad += 1
	elif(sexo == "F" and idade < 20):
		mulheres20 += 1
	if(idade >= 18):
		pessoasMais18 += 1

	if(continuar == "N"):
		break

print(f"Homem cadastrados {homemCad}")
print(f"Pessoas com mais de ou igual a 18 anos {pessoasMais18}")
print(f"Mulheres com menos de 20 anos {mulheres20}")
