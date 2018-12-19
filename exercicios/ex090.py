aluno = {}
aluno["nome"] = input("Digite um nome: ").strip()
aluno["media"] = float(input(f"Digite a média da pessoa {aluno['nome']}: ").strip())

if(aluno["media"] > 7):
	aluno["situacao"] = "Aprovado"
elif(aluno["media"] > 5):
	aluno["situacao"] = "Recuperação"
else:
	aluno["situacao"] = "Reprovado"
	
print(f"O aluno {aluno['nome']} tem média {aluno['media']} com situação {aluno['situacao']}")