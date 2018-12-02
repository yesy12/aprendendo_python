numero =int(input("Digite um numero: "))

uni = numero//1 %10
dez = numero//10 %10
cen = numero//100 %10
mil = numero//1000 %10

print("numero escolhido {:.0f}".format(numero) )
print("Unidade {}".format(uni) )
print("Dezena {}".format(dez) )
print("Centenza {}".format(cen) )
print("Milhar {}".format(mil) )
