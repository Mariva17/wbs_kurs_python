"""
Filter - Funktion

filter(func, seq)
"""

values = [1, 111, 12, 124, 654]

result = filter(lambda x: x > 100, values)
print(list(result))

# als List - Comprehension
result = [x for x in values if x > 100]
print(result)



