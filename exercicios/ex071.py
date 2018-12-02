print("CAIXA SIMULATOR")

valor = int(input("Digite seu valor: "))
nota = 100
qtdNota = 0 

while valor > 0 :
	valor -= nota 
	qtdNota += 1
	
	if(nota > valor):
		print(f"A nota de R$ {nota} tem {qtdNota} notas")
		nota = 50
		qtdNota = 0
		if(nota > valor):
			nota = 20
			qtdNota = 0
			if(nota > valor):
				nota  = 10
				qtdNota = 0
				if(nota > valor):
					nota = 5
					qtdNota = 0
					if(nota > valor):
						nota = 1
						qtdNota = 0
		
