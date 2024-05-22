"""
Binary Search.

"""
import random
from timeit import timeit
import bisect


def get_dataset(pop_size: int, k: int) -> list:
    return sorted(random.sample(list(range(pop_size)), k=k))


def naive_search(array, element) -> int:
    for index, el in enumerate(array):
        if element == el:
            return index
    return -1


def binary_search(array, element, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if element == array[mid]:
        return mid
    if element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)


def search_binary(dataset, suchzahl):
    return binary_search(dataset, suchzahl, 0, len(dataset) - 1)
    

def search_naive(dataset, suchzahl):
    return naive_search(dataset, suchzahl)
    



#dataset = sorted([22, 11, 8, 3, 21, 143, 78])
dataset = get_dataset(pop_size=10**6, k=500_000)
#suchzahl = 8   # index 8 = 1
suchzahl = dataset[-1]

print(f"Gesucht wird nach: {suchzahl}")

# result = binary_search(dataset, suchzahl, 0, len(dataset)-1)
# print("result: ", result)
# result2 = naive_search(dataset, suchzahl)
# print("native search:" , result2)

# Timeit:
result = timeit("search_binary(dataset, suchzahl)", globals=globals(), number=10**3)
print("Result Binary Search:", result)

result = timeit("search_naive(dataset, suchzahl)", globals=globals(), number=10**3)
print("Result Naive Search:", result)