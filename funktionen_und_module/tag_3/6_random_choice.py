"""
choice (1.Element ziehen)
choices (k Elemente ziehen)
"""

import random



random.seed(42)

rabbits = [
    "fiver",
    "hazel",
    "bigwig",
]

# choice => ein Element ziehen
random_rabbit = random.choice(rabbits)
print(random_rabbit)

print("*"*30)

# choices => k Elemente ziehen
# mit Zurücklegen
weights = (10, 20, 60)
random_rabbit = random.choices(rabbits, weights=weights, k=8)
print(random_rabbit)
