#!/usr/bin/python3.6
import rond

while 1:
	v = input("\t\nChoisissez un rayon: ")

	if v == "q" or v == "quit" or v == "exit":
		exit()
	
	if not v.isnumeric():
		print("\t\nQue des chiffres svp.")
		continue
	v = int(v)
	ptitRond = rond.rond(v)
	print(f"\t\nAir du ptit rond = {ptitRond.CalculAir()}")
	print(f"\t\nPerimetre du ptit rond = {ptitRond.CalculPerimetre()}")


