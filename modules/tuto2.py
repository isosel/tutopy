#!/usr/local/bin/python3.10		#SHEBANG
import math

def tablex(a,b,c):
	v = int(c/10)
	for i in range(b,c+1):
		digits = int(i/10)
		txt = (v-digits)*" "
		txt = txt + f"{i}x{a}={i*a}"
		
		print(txt)	
		
