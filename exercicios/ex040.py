nota1 = float(input("Digite uma nota: ").strip())
nota2 = float(input("Digite outra nota: ").strip())
media = (nota1+nota2)/2

if(media <= 5):
	print("Reprovado")
elif(media > 5 and media <=6.9):
	print("Recuperação")
elif(media >= 7):
	print("Aprovado")
