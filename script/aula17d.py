valores = list(range(5,10))
print(valores)

valores = [26,72,38,274,274,3729]
print("\n")
print(f"Ordem normal \n{valores}")

valores.sort()
print(f"\nEm ordem \n{valores}")

valores.sort(reverse=True)
print(f"\nEm ordem Ao contrária \n{valores}")