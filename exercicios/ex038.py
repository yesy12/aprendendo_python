n1 = int(input("Digite um numero: ").strip())
n2 = int(input("Digite outro numero: ").strip())

if(n1>n2):
	print("{} é maior que {}".format(n1,n2))
elif(n2>n1):
	print("{} é maior que {}".format(n2,n1))
elif(n1==n2):
	print("{} é igual a {}".format(n1,n2))
