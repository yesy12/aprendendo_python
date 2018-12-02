from math import ceil
print("Minha casa minha vida\n")

valor = int(input("Digite o valor da casa: ").strip())
sal = int(input("Digite o seu salário: ").strip())
anos = int(input("Digite em quantos anos para pagar: ").strip())

meses = anos*12
sal30 = sal*0.3
prestacao = ceil(valor/meses)

if(sal30 >= prestacao):
	print("\nVocê esta apto a parcelar sua casa com mensalidades de R$ {} em {} meses ".format(prestacao,meses))
else:
	print("\nVocê não esta apto a parcelar sua casa no valor de R$ {} em {} meses recebendo R$ {} pois a parcela fica R$ {}".format(valor,meses,sal,prestacao))
