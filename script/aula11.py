a = 4

cores={
"limpa":"\033[m","azul":"\033[34m",
"amarelo":"\033[33m"
}

print("O valor {1}{0}{2}".format(a,cores['azul'],cores['limpa'] ))
