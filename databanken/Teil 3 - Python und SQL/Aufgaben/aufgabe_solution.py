import mysql.connector as mc
import mysql
from sys import exit


def add_data(cursor, connection, name, nummer, price, stock):
    sql = """INSERT INTO katalog (Produktname, Artikelnummer, Netto_Price, stock) VALUES (%s, %s, %s, %s)"""
    params = (name, nummer, price, stock)
    cursor.execute(sql, params)
    connection.commit()


def show_data(cursor):
    sql = """SELECT * FROM katalog"""
    cursor.execute(sql)
    result = cursor.fetchall()
    print("*" * 40)
    for id, name, nummer, price, stock in result:
        print(f"{id} \t {name} \t{nummer} \t{price} \t{stock}")
    print("*" * 40)


def delete_data(cursor, connection, name):
    try:
        sql = """DELETE FROM katalog WHERE Produktname = %s"""
        cursor.execute(sql, (name,))
        connection.commit()
    except:
        print("This data does not exist")


def add_new_column(cursor, connection, name):
    try:
        sql = f"""ALTER TABLE katalog ADD COLUMN {name} VARCHAR(30)"""
        cursor.execute(sql)
        connection.commit()
    except:
        print("This column is already exists")


def menu():
    print(
        "\tA / a: Vorhandene Tabellen anzeigen\n",
        "\tB / b: Daten hinzufügen\n"
        "\tE / e: End\n"
        "\tD / d: Delete item\n"
        "\tC / c: Add new column\n"
    )


def main():
    try:
        connection = mc.connect(
            host='localhost',
            user='root',
            password='12345',
        )

    except mc.errors.ProgrammingError as e:
        print("Es ist folgende Fehler aufgetreten: \n ", e)

    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS store")
        cursor.execute("USE store")
        sql = """CREATE TABLE IF NOT EXISTS katalog(
        id INT AUTO_INCREMENT PRIMARY KEY,
        Produktname VARCHAR(30) NOT NULL,
        Artikelnummer VARCHAR(30) NOT NULL,
        Netto_Price FLOAT (7, 2))"""
        cursor.execute(sql)
    except mc.errors.ProgrammingError as e:
        print("Es ist folgende Fehler aufgetreten: \n ", e)

    while True:
        menu()
        ui = input("-> ").upper()
        if ui == "E":
            break
        elif ui == "A":
            show_data(cursor)
        elif ui == "B":
            name = input("Produktname: ")
            nummer = input("Artikelnummer: ")
            price = input("Netto_Price: ")
            stock = input("Stock: ")
            add_data(cursor, connection, name, nummer, price, stock)
        elif ui == "D":
            delete_data(cursor, connection, "chair")
        elif ui == "C":
            add_new_column(cursor, connection, "stock")

    connection.close()


if __name__ == "__main__":
    main()
