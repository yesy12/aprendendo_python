peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/altura**2

if(imc < 18.5):
	print("Você esta abaixo do peso")
elif(imc >= 18.5 and imc < 25):
	print("Você esta no peso ideal")
elif(imc >= 25 and imc < 30):
	print("Você esta com sobrepeso")
elif(imc > 30 and imc < 40):
	print("Você esta com Obesidade")
elif(imc >=40):
	print("Você está com Obesidade mórbida")
