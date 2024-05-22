values = [1, 2, 4, 8, 19]
values = sorted(values)
anzahl = len(values)

if not anzahl % 2:
    median = (values[anzahl // 2 - 1] + values[anzahl // 2]) / 2
else:
    median = values[anzahl // 2]
print(median)