import mysql.connector as mc
import mysql
from sys import exit


USER = "root"
HOST = "localhost"
PWD = "12345"
def create_db(*, user=USER, host=HOST, pwd=PWD, database="warenkatalog_new") -> None | mc.Error:
    """Creates database at given host for given user."""
    try:
        connection = mc.connect(
            host=host,
            user=user,
            password=pwd,
        )
        c = connection.cursor()
    except mc.errors.ProgrammingError as e:
        print("Error: %s" % e)
        return e

    try:
        c.execute(f"""CREATE DATABASE IF NOT EXISTS {database}""")
        # print("Database created successfully")
    except mc.Error as e:
        print("Error: %s" % e)
        return e
    finally:
        connection.close()

create_db()




def add_data(c, connection, name, nummer, preis):
    sql = """INSERT INTO warentabelle (Produktsname, Artikelnummer, Netto_Preis) values (%s, %s, %s)"""
    c.execute(sql,(name,nummer,preis))
    connection.commit()

def show_data(c):
    c.execute("SELECT * FROM warentabelle")
    print("*" * 40)
    print("ID","Produktsname","Artikelnummer","Netto_Preis")
    for id,name,nummer,preis in c.fetchall():
        print(f"{id}\t{name}\t{nummer}\t{preis}")
    print("*" * 40)

def menu():
    print(
        "\tA / a: Vorhandene Tabellen anzeigen\n",
        "\tB / b: Daten hinzufügen\n"
        "\tE / e: End"
    )


def main():
    try:
        connection = mc.connect(
            host='localhost',
            user='root',
            password='12345',
        )
    except:
        print("Connection failed")

    try:
        c = connection.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS warenkatalog")
        c.execute("USE warenkatalog")
        sql = """CREATE TABLE IF NOT EXISTS warentabelle (
        ID INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
        Produktsname VARCHAR(30) NOT NULL,
        Artikelnummer VARCHAR(30) NOT NULL,
        Netto_Preis VARCHAR(30) NOT NULL)"""
        c.execute(sql)
    except mc.errors.ProgrammingError as e:
        print("Es ist folgender Fehler aufgetreten: \n", e)

    while True:
        menu()
        user_input = input("-> ").upper()
        if user_input == "E":
            break
        elif user_input == "A":
            show_data(c)
        elif user_input == "B":
            name = input("Produktsname: ")
            nummer = input("Artikelnummer: ")
            preis = input("Netto-Preis: ")
            add_data(c,connection,name,nummer,preis)

    connection.close()

if __name__ == "__main__":
   main()