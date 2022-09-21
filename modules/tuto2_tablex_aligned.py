#!/usr/local/bin/python3.10		#SHEBANG
from math import log10
'''
add spaces at the begening depending the value of c and i 
to keep things aligned
'''
def tablex(a,b,c):
	digitmax = int(log10(c))+1
	for i in range(b,c+1):
		digit = int(log10(i))+1
		txt = (digitmax-digit)*" "
		txt = txt + f"{i}x{a}={i*a}"
		
		print(txt)	
		
