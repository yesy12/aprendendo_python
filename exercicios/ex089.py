#alunos = [ [nome,[nota1,nota2,media]] 
alunos = []
print("nome e media em lista")
while True:
	nome = input("Digite o nome do Aluno: ").strip()
	nota1 = int(input(f"Digite a nota1 do {nome}: ").strip())
	nota2 = int(input(f"Digite a nota2 do {nome}: ").strip())
	media = (nota1+nota2)/2

	alunos.append([nome,[nota1,nota2,media] ])
	
	cont = input("Você deseja continuar?[s/n] ").strip().upper()
	if(cont == "N"):
		break
		
print("Posição NOME MEDIA".format(" "," "))
for pos,aluno in enumerate(alunos):
	print("{} {} {}".format(pos,aluno[0],aluno[1][2]))
	
while True:
	numero = int(input("Digite o número para ver as notas e 999 para sair: "))
	if(numero == 999):
		break
	print(f"O aluno {alunos[numero][0]} tem as notas {alunos[numero][1][:2]}")