from time import sleep
from emoji import emojize

for c in range(10,0,-1):
	print(c)
	sleep(1)

print(emojize(":rocket: :bomb:",use_aliases=True))
