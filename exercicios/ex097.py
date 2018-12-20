def escreva(txt):
	tamanho = len(txt) +6
	print("-" * tamanho)
	print(f"   {txt}")
	print("-" * tamanho)

frase = input("Digite uma frase: ").strip()

escreva(frase)