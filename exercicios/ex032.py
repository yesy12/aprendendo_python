print("Verificar ano bissexto")
ano =int(input("digite um ano para verificar o ano: ").strip())

if(ano%4==0):
	print("{} é bissexto".format(ano))
else:
	print("{} não é bissexto".format(ano))
