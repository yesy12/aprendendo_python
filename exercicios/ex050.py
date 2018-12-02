s=0
for a in range(0,6):
	n = int(input("Digite um numero ({}/6): ".format(a+1)))
	if(n % 2 == 0):
		s+=n

print("deu ao todo {}".format(s))
