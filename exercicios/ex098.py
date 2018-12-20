from time import sleep

def contador(inicio,fim,passo):
	if(passo == 0):
		passo = 1
	if(passo < 0):
		passo *= -1
	
	print(f"Inicio {inicio} para chegar em {fim} pulando de {passo} em {passo}")
	sleep(1)
	
	if(inicio < fim):
		while inicio <= fim:
			print(f"{inicio} ",flush=True,end="")
			inicio += passo
			sleep(0.15)
		for a in range(0,2):
			print()
			
	elif(inicio > fim):
		while inicio >= fim:
			print(f"{inicio} ",flush=True,end="")
			inicio -= passo
			sleep(0.15)
		for a in range(0,2):
			print()
		
contador(1,10,1)
contador(10,0,2)

inicio = int(input("Digite um inicio: "))
fim = int(input("Digite um fim: "))
passo = int(input("Digite um passo: "))

contador(inicio,fim,passo)