#!/usr/bin/python3.6
#-*-coding:UTF-8-*-

liste = ["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
print("Liste normale:")
for a in liste:
	print(f"\t\n{a}") 

liste.reverse()
print("Liste reverse:")
for a in liste:
	print(f"\t\n{a}") 

liste.sort()
print("Liste triée:")
for a in liste:
	print(f"\t\n{a}") 

liste_domestique = ["chat", "chien", "chiot"]
for dom in liste_domestique:
	liste.remove(dom)
liste.append("troll")
print(f"\t\nListe sans animaux domestiques: {liste}")
