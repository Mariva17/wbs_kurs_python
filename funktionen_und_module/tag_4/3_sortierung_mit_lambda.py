"""
Sortieren von dict

"""

d = {
    "a": {"value": 22, "number": 53, "mode": {"x": 3}},
    "b": {"value": 52, "number": 31, "mode": {"x": 2}},
    "c": {"value": 12, "number": 123, "mode": {"x": 1}},
}
sorted_d = sorted(d.items(), key=lambda el: el[1]["number"])
print(sorted_d)

sorted_nach_x = sorted(d.items(), key=lambda el: el[1]["mode"]["x"])
print(sorted_nach_x)