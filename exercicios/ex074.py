from random import randint

n1 = randint(-10,10)
n2 = randint(-10,10)
n3 = randint(-10,10)
n4 = randint(-10,10)
n5 = randint(-10,10)

tupla = (n1,n2,n3,n4,n5)

print(f"Números gerados {tupla}")
print(f"Menor valor {min(tupla)}")
print(f"Maior valor {max(tupla)}")
