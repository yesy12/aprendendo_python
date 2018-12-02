pa = []

p1 = int(input("digite um numero para a pa: ").strip())
pa.append(p1)
razao = int(input("Razão da pa: ").strip())

print("Por padrão são 10 termos")
continuar = input("Digite se você deseja colocar a quantidade de termos [s/n]? ").strip().upper()

if(continuar == "S"):
	termos = int(input("Digite a quantidade de termos que deseja: ").strip())
elif(continuar == "N"):
	termos = 10

for a in range(0,termos-1):
	valor = pa[a] + razao
	pa.append(valor)

print(f"Os termos são ({pa}) \n{len(pa)}")
print(f"Com razão de {razao}")