sal =int(input("Digite o salário: "))

if(sal >1250):
	aumento=0.1
else:
	aumento=0.15

salNovo=str(sal*aumento+sal).replace(".",",")
aumento=aumento*100
print("Seu salário antigo é R$ {}".format(sal))
print("Seu salário com aumento de {:.0f}% é R$ {}".format(aumento,salNovo))


