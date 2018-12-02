fibonacci = [0,1]

print("Sequência fibonnaci")
n = int(input("Digite um numero: "))
	
for a in range(1,n):
	fibonacci.append(fibonacci[a-1] + fibonacci[a])
	
	
print(fibonacci)	