#!/usr/bin/python3.6
from time import sleep

quit = False
quittuple = ('q','quit','exit','quitter')

def convertCintoF(a):
	return a*9/5+32

def convertFintoC(a):
	return (a-32)*5/9

while(quit == False):
	txt = input("\t\nEntrez une température svp: ")
	
	if txt in quittuple :
		print("\t\nOk!")
		quit = True
		sleep(1)
		continue

	print("\t\nOn continue.")

	if not txt[0].isnumeric():
		print("\t\nFormat invalide... exemple: 12C ou 45F")
		sleep(1)
		continue
	
	if txt[-1] == 'C' or txt[-1] == 'c':
		txt = txt[:-1]
		temp = convertCintoF(int(txt[:len(txt)]))
		print(f"\t\n{txt}C = {temp}F")
	elif txt[-1] == 'F' or txt[-1] == 'f':
		txt = txt[:-1]
		temp = convertFintoC(int(txt[:len(txt)]))
		print(f"\t\n{txt}F = {temp}C")
	else:
		print("\t\nFormat inconnu. Utilisez seulement 'F' ou 'C'.")
		
print("==== END ====")
