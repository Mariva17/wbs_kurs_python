"""
Zufällige floats mit random
Zahl zwischen 0 und 1 (exclusive)
"""

import random


random.seed(42)

# Zufallzahl zwischen 0 und 1
x = random.random() # 0.6394267984578837
print(x)

# Zufallzahl zwischen min und max
y = random.uniform(3, 5) # 3.050021510445334
print(y)