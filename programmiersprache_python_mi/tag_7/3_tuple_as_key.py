"""
Tuple als Key Eines Dicts

"""

game = {}
key = (1, 2)
invalid_key = [1, 2]

# Tuple mit Liste als Element ist nicht mehr hashable und deshalb
# auch nicht als Key eines Dict zu verbraucht
invalid_key = [1, 2, [3, 4]]
invalid_key[2].append(5)
print(invalid_key)

# game[key] = 100 # Tuple dient hier als Key für da dict game
game[invalid_key] = 100
# print(game)

