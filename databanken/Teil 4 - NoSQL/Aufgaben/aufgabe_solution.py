import pymongo
from pymongo import MongoClient
from sys import exit


def create_database():
    client = MongoClient('mongodb://localhost:27017')
    db = client["neueDatenbank"]
    return db


def create_collection_products():
    db = create_database()
    collection = db["products"]
    return collection


def add_data():
    product_name = input("Bitte geben Sie Produktname ein: ")
    artikel = input("Bitte geben Sie Artikelnummer ein: ")
    netto_price = float(input("Bitte geben Sie Nett_price ein: "))
    stock = input("Bitte geben Sie Anzahl ein: ")

    collection = create_collection_products()
    produkt = {"Produktname": product_name, "Artikel": artikel, "Netto_price": netto_price, "Stock": stock}
    collection.insert_one(produkt)
    print("Produkt hinzugefügt")


def show_data():
    collection = create_collection_products()
    data = collection.find()

    for product in data:
        for key, value in product.items():
            print(f"{key}: {value}")
        print("*" * 40)


def show_specific_data():
    collection = create_collection_products()
    key_word = input("Bitte geben Sie Name von data ein: ").title()
    name = input("Bitte geben Sie data ein: ")
    data = collection.find_one({key_word: name})
    print(data["Produktname"])
    print(data["Artikel"])
    print(data["Netto_price"])
    print(data["Stock"])


def delete_specific_data():
    collection = create_collection_products()
    key_word = input("Bitte geben Sie data ein: ").upper()
    name = input("Bitte geben Sie Name von data ein: ")
    res = collection.delete_one({key_word: name})
    if res.deleted_count > 0:
        print("Data deleted")
    else:
        print("Data nicht gefunden")


def update_produkt_in_collection():
    collection = create_collection_products()
    artikel_produkt = input("Bitte geben Sie Artikelnummer des Produkts ein: ")
    produkt = collection.find_one({"Artikel": artikel_produkt})

    if produkt:
        update_produkt = {}
        neue_name = input("Bitte geben Sie neuer Name von Produkt ein oder nichts: ")
        neue_artikel = input("Bitte geben Sie neuer Artikel von Produkt ein oder nichts: ")
        neue_price = float(input("Bitte geben Sie neue Netto_Price von Produkt ein oder nichts: "))
        neue_stock = input("Bitte geben Sie neue Menge von Produkt ein oder nichts: ")

        if neue_name:
            update_produkt["Produktname"] = neue_name
        if neue_artikel:
            update_produkt["Artikel"] = neue_artikel
        if neue_price:
            update_produkt["Netto_price"] = neue_price
        if neue_stock:
            update_produkt["Stock"] = neue_stock

        if update_produkt:
            collection.update_one({"Artikel": artikel_produkt}, {"$set": update_produkt})
        else:
            print("Keine Änderungen vorgenommen")

    else:
        print("Data nicht gefunden")


def main():
    list_command = ["Produkt hinzufügen", "Produkt ändern", "Produkte auflisten", "Specific Produkt auflisten",
                    "Produkt löschen", "Programmende"]
    for elem, i in enumerate(list_command, 1):
        print(f"{elem} \t{i}")
    while True:
        choice = input("Bitte treffen Sie einen Auswahl: ")
        match choice:
            case "1":
                add_data()
            case "2":
                update_produkt_in_collection()
            case "3":
                show_data()
            case "4":
                show_specific_data()
            case "5":
                delete_specific_data()
            case "6":
                print("Auf Wiedersehen!")
                exit()


if __name__ == "__main__":
    main()
