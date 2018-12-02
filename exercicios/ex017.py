from math import sqrt
catOp=float(input("digite o cateto oposto: "))
catAd=float(input("digite o cateto adjancente: "))

hipot = catOp**2  + catAd**2
hipot = sqrt(hipot)

print("A hipotenusa de {} e {} é {:.4f} ".format(catOp,catAd,hipot))
