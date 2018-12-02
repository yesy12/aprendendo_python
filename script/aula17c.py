lanche = [ "Hamubrguer","Suco","Pizza","Pudim"]
print("lista normal")
lanche.append("Cookie")
lanche.insert(0,"Pavê")
print(lanche)

print(f"\nfoi removido {lanche[3]}")
del(lanche[3])
print(lanche)

if( "Cookie" in lanche):
	print("\nFoi removido Cookie")
	lanche.remove("Cookie")

print(lanche)