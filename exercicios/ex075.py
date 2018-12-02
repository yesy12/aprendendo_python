n1 = int(input("Digite um numero: ").strip())
n2 = int(input("Digite outro numero: ").strip())
n3 = int(input("Digite mais outro numero: ").strip())
n4 = int(input("Digite finalmente outro numero: ").strip())

tupla = (n1,n2,n3,n4)
pares = 0

print(f"Quantidade de '9' foram {tupla.count(9)} vezes")
if( 3 in tupla):
	print(f"Apareceu 3 na posição {tupla.index(3)}°")
else:
	print("Não existe 3 ")

for n in tupla:
	if(n % 2 == 0):
		pares += 1

print(f"Foram digitados {pares} pares")