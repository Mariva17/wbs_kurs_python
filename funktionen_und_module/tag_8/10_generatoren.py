"""
Generator-Expressions: erzeugt einen Iterator
(x for x in range(100))
"""
import os
import psutil

process_id = os.getpid()
process = psutil.Process(process_id)

print("current memory:", process.memory_info().rss / 1024**2)
n = [(i, i**2) for i in range(10**6)]
print("current memory:", process.memory_info().rss / 1024**2)
print(n[:3])
n = None

print("current memory:", process.memory_info().rss / 1024**2)
m = ((i, i**2) for i in range(10**6)) # erzeugt einen Iterator
print(m)
print("current memory:", process.memory_info().rss / 1024**2)

map_object = map(lambda x: x, range(10**7))
print("current memory:", process.memory_info().rss / 1024**2)



