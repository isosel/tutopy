#!/usr/local/bin/python3.10
#use 'sudo chmod u+x file.py" to enable its execution
#help <modulename> to get the manual of the module


"""
Description of the module, for documentation purposes
We can describe all functions, contents, actions, return... 
"""

import math, random
#from math import pow, log
#from random import seed, random
#import math as m, random as r

random.seed(None)
value = random.random()

logv = math.log(value)
abslog = math.pow(logv, 2.0)

print(f"abslog: {abslog}")


