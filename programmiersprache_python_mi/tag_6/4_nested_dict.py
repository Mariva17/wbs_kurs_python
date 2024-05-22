"""
Verschachteltes Dict (nested)

"""
import json

cities = {
    "dortmund": {
        "info": {
            "population": 400000,
            "state": "North Rhine-Westphalia"
        },
    },
    "bielefeld": False,
}
print(cities)
print(cities["dortmund"]["info"]["population"])
print(cities.get("dortmund").get("info").get("population"))

# Umformen eines Dicts in einen Json-String
json_string = json.dumps(cities)
print(json_string)

