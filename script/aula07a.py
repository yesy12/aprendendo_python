nome = input('qual é seu nome?: ')
print('prazer em conhecer voce {:_^15}|'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1*n2
d = n1*n2
me = n1-n2
pot = n1**n2
resto = n1%n2

print("a soma de {} e {} vale {}".format(n1,n2,s))
print("a multiplicacao de {} e {} vale {}".format(n1,n2,m))
print("divisao vale {:.3f}".format(d))
print("subtracao vale {}".format(me))
print("potencia vale {}".format(pot))
print("resto vale {}".format(resto))
