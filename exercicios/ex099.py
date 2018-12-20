from time import sleep

def maior(*num):
	print("\nAnálise dos Maiores valores")
	if(len(num) >0):
		maior = 0
		for pos,valor in enumerate(num):
			if(pos == 0):
				maior=valor
			else:
				if(maior < valor):
					maior = valor
		print("Nos números ",end="")
		for n in num:
			print(f"{n} ",end="",flush=True)
			sleep(0.35)
		print(f"O maior valor é {maior}",end="")		
		print()
	else:
		print("0 é maior valor por não existir nenhum número")

maior(2,3,5,6,7,-10)
maior(-2,-30,-23,-34)
maior()