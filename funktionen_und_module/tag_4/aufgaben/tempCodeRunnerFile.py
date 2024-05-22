numbers = [2, 3, 4, 5, 6]
#gerade_zahlen = list(filter(lambda x: x % 2 == 0, numbers))
values_new_2 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))) # in einer Ziele

print("Result: ", values_new_2)
