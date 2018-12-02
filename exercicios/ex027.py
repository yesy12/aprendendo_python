nome=input("Digite seu nome completo: ").strip()

print("Seu nome é {}".format(nome))
nomePri=nome.split()
print("Seu primeiro nome é {}".format(nomePri[0]) )
print("Seu ultimo nome é {}".format( nomePri[len(nomePri)-1] ))
