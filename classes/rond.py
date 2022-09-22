#!/usr/bin/python3.6
import math

class rond():	
	def __init__(self, rayon):
		self.rayon = rayon
	
	def CalculAir(self):
		return self.rayon**2*math.pi

	def CalculPerimetre(self):
		return self.rayon*2*math.pi

