valor = cont = soma = 0

while True:
	valor = int(input("Digite um valor: ").strip())
	if(valor == 999):
		break
	cont += 1
	soma += valor

print(f"A soma foi {soma}")
print(f"A quantidade vezes foi {cont}")
