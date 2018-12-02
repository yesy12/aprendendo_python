ano = 2018
anoPergunta = int(input("Digite seu ano de nascimento: "))
idade = ano-anoPergunta

if(idade == 18):
	print("Na hora de servir")
elif(idade > 18):
	print("Você já deveria te servido,se não va procurar resolver isso")
elif(idade < 18):
	print("Faltam {} anos para você servir".format(18-idade) )
