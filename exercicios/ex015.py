dias=int(input("Quantos dias com o carro?: "))

kms= float(input("Quantos Kms com o carro?: "))

valorDia=dias*60

valorKm=kms*0.15

valorTotal =valorDia+valorKm

print("O total é de R$ {:.2f} pelo o carro".format(valorTotal))
