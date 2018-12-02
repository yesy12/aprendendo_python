from math import ceil
height = float(input("Digite a altura da parede: "))
width = float(input("Digite o comprimento da parede: "))

area = height*width

qtd=ceil(area/2)

print("Vai precisa de {:.0f} de lata de tintas ".format(qtd))
