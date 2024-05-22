"""

Listen Abstraktion (List comprehensions)
"""

seq = [2, 4, 7, 8]

# Liste mit Quadraten der Zahlen von seq

# klassisch
seq_quad = []
for el in seq:
    seq_quad.append(el**2)

print(seq_quad)

# via List comprehension
seq_quad = [el**2 for el in seq]
print(seq_quad)

# direkt nutzen bei Funktionsaufruf
sum(el**2 for el in seq)
