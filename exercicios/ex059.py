opcao = 0

while opcao != 5:
	n1 = int(input("Digite um numero: ").strip().upper())
	n2 = int(input("Digite outro numero: ").strip().upper())
	print("""Opções a seguinte
	[1] para somar
	[2] para multiplicar
	[3] para maior
	[4] para novos numeros 
	[5] para sair """)
	opcao = int(input("Digite a opção: "))
	if(opcao == 1):
		print("A soma entre {} e {} = {}".format(n1,n2, n1+n2))
	elif(opcao == 2):
		print("A multiplicação entre {} e {} é igual a {}".format(n1,n2,n1*n2))
	elif(opcao == 3):
		if(n1 > n2):
			maior = n1
			menor = n2
		else:
			maior = n2
			menor = n1
		print("{} é > {}".format(maior,menor))
