nome = input("Digite seu nome completo: ").strip()

print("TODAS LETRAS MAIÚSCULAS ('{}')".format(nome.upper() ))
print("todas letras minúsculas ('{}')".format(nome.lower() ))
frase=nome.replace(" ","")
print("Tamanho do seu nome ('{}')".format(len(frase) ))

tamanho=nome.split(" ")
print("Tamanho de '{1}' ('{0}')".format(len(tamanho[0]),tamanho[0] ))
