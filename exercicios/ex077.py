palavras = ("programador","limao","computador",
"comida","liquidificador","panela","nescau",
"teclado")

for palavra in palavras:
	print(f"A palavra {palavra} tem as vogais ",end="")
	for letras in palavra:
		if(letras == "a" or letras == "e" or letras == "i" or letras == "o" or letras == "u"):
			print(f" {letras}",end="")	
	print("\n")		  