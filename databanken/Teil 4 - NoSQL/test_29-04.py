from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["neueDatenbank"]
collection = db["meineCollection"]

name = input("Bitte geben Sie einen Namen ein: ")

result = {"name": {"$regex": f".*{name}.*"}}

try:
    ergebnis = collection.find(result)
    for i in ergebnis:
        print(i)
except Exception as e:
    print("Es ist folgende Fehler aufgetreten", e)
finally:
    client.close()
