import sqlite3

name_file = "telefonbuch-new.db"
table_name = "users_list"


conn = sqlite3.connect(name_file)  # Verbindung zur Datenbank, wird erstellt, wenn nicht vorhanden
c = conn.cursor()  # Ein cursor wird erstellt
conn.close()
def new_table(filename, table):
    conn = sqlite3.connect("telefonbuch-new.db")
    c = conn.cursor()
    sql = """create table IF NOT EXISTS users_list
    (
        ID       integer
        primary key,
        vorname  text,
        nachname text,
        telefon  text
    );
    """
    c.execute(sql)  # SQL wird ausgeführt
    conn.commit()
    conn.close()  # SQL-Befehl wird bestätigt


def fill_table():
    conn = sqlite3.connect(name_file)
    c = conn.cursor()
    print(
        "Welcome to new phonebook! \n If you want start press any key. \n If you want exit from programm, type 'stop' or 'exit'.")
    stop_words = ["stop", "exit", "quit"]
    ui = input()
    while True:
        vorname = input("Bitte geben Sie den Vornamen ein: ")  # Ihr Code HIER!!!
        nachname = input("Bitte geben Sie den Nachnamen ein: ")  # Ihr Code HIER!!!3
        telefonnummer = input("Bitte geben Sie den Telefonnummer ein: ")
        params = (vorname, nachname, telefonnummer)
        sql = """INSERT INTO users_list (vorname, nachname, telefon) VALUES (?, ?, ?)"""

        c.execute(sql, params)
        conn.commit()
    else:
        conn.close()


def find_number(username, filename):
    conn = sqlite3.connect(name_file)
    c = conn.cursor()
    params = (username,)
    sql = """SELECT telefonnummer FROM filename  WHERE nachname=username;"""
    result = c.execute(sql, params).fetchall()
    return print(result)


def main():
    name_file = "telefonbuch-small.db"
    table_name = "users_list"
    table_name1 = new_table(name_file, table_name)
    data = fill_table(table_name1)
    res = find_number("Smith", data)
    conn.close()
    return res


main()

