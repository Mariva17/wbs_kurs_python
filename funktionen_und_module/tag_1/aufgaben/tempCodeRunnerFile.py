values = [2, 2.2, 4, 2.3, 0.1]
interval = (1, 5.3)

def check_values(val, interval):
    a, b = interval
    result = all(a <= value <= b for value in val) 
    print(result)


result = check_values(values, interval)
print(result)
