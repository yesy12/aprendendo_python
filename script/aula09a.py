frase="Curso em Video Python"
print("fatiamento de string da frase '{}'".format(frase))
print("\n")

print("[n] n é a posição da variavel ({1}) '{0}'".format(frase[9],9 ))

print("[n:p] p é onde vai terminar ({1}:{2})  '{0}'".format(frase[3:7],3,7 ))

print("[n:p:d] d é onde será pulado de quanto em quanto ({1}:{2}:{3})'{0}'".format(frase[0:15:2],0,15,2 ))


print("\ncomprimento len() de frase é '{}'".format(len(frase)))


print("\nconta quantas vezes aparece determinada letra .count('letra'),'{}'".format(frase.count('o')))
print("\n")

print(frase.find('Pyt'),"diz a posicao da questão .find")
print("\n")

print("Cursso" in frase,"sabe se existir na string 'frase' in variavel")
