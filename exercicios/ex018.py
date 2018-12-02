from math import sin
from math import cos
from math import tan
from math import radians

ang=int(input("Digite um angulo: "))
radianos =radians(ang)

print("O angulo {} tem seno de {:.4f}".format(ang,sin(radianos)))

print("O angulo {} tem cosseno de {:.4f}".format(ang,cos(radianos)))

print("O angulo {} tem tangente de {:.4f}".format(ang,tan(radianos)))
