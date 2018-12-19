estado = {}
brasil = []

for c in range(0,3):
	estado ["uf"] = input("Digite a união federativa: ")
	estado ["sigla"] = input("Digite a sigla do Estado: ")
	brasil.append(estado.copy())
	
print(brasil)