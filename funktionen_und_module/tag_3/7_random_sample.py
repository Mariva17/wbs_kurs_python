"""

Ziehen OHNE Zurücklegen mit sample

"""

import random

random.seed(42)

rabbits = [
    "fiver",
    "hazel",
    "bigwig",
    "blackberry",
]

# mit count kann man angeben, wie häuftig ein Element in der 
# Population vorhanden ist 
random_population = random.sample(rabbits, counts=[100, 3, 1, 7], k=42)
print(random_population)

random.shuffle(random_population)
