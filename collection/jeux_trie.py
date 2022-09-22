#!/usr/bin/python3.6
#-*- coding : UTF-8 -*-
import random
tabjeux = []
for i in range(0, 10):
	tabjeux.append(random.randint(1, 10))
tabjeux.sort()
print(tabjeux)
iswon=False
while 1:
	val = input("\t\nChoisissez une valeur:")
	if not val.isnumeric():
		continue
	val = int(val)
	index=0
	for i in tabjeux:
		index = index + 1
		print(f"index boucle:{index}")
		if i == val:
			print("Gagné")
			iswon=True
			break
		if i > val:
			print(f"{i}>{val}")
			break
	if iswon:
		break;
	else:
		print("perdu")
		break
