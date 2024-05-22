"""
Zufällige Ganzenzahlen mit randint or randrange

"""

import random

# Randint
x = random.randint(2, 10)
print(x)

print("*" * 30)

# Rand-Range:   start-stop (Exclusive) - step
x = random.randrange(10, 20, 2)
print(x)