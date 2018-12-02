pa = []

p1 = int(input("digite um numero para a pa: ").strip())
pa.append(p1)
razao = int(input("Razão da pa: ").strip())

for a in range(0,9):
	valor = pa[a] + razao
	pa.append(valor)

print(f"Os termos são ({pa})")
print(f"Com razão de {razao}")