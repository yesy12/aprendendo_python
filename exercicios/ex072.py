numeros = ("zero","um","dois","três","quatro","cinco","seis","sete",
"oito","nove","dez","onze","doze","treze","cartões","quinze","dezeseis",
"dezesete","dezoito","dezenove","vinte")

print("Números por extenso")

n =int(input("Digite o número: "))
if(n >= 0 and n < 21):
	print(numeros[n])