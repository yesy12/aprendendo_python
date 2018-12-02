valor = int(input("Digite seu valor: "))
print("""BASES DE CONVERSÃO
1 para binário
2 para octal
3 para hexadecimal
""")
opcao = int(input("Digite sua opção: "))

if(opcao == 1):
	print("{} em BINÁRIO é {}".format(valor,bin(valor)[2:] ))
elif(opcao == 2):
	print("{} em OCTAL é {}".format(valor,oct(valor)[2:] ))
elif(opcao == 3):
	print("{} em HEXADECIMAL {}".format(valor,hex(valor)[2:] ))
else:
	print("ERRO")
