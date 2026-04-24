import psycopg2
import csv
from connect import connect

# CREATE TABLE
def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


# INSERT single contact
def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


# INSERT from CSV
def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()


# SELECT (read all)
def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# UPDATE contact
def update_contact(name, new_phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()


# DELETE contact
def delete_contact(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()


# SEARCH
def search_contact(keyword):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s OR phone LIKE %s",
        (f"%{keyword}%", f"%{keyword}%")
    )

    print(cur.fetchall())

    cur.close()
    conn.close()


# SIMPLE MENU (console app)
def menu():
    create_table()

    while True:
        print("\n1. Add contact")
        print("2. Show contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Search")
        print("6. Import CSV")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            name = input("Name: ")
            phone = input("New phone: ")
            update_contact(name, phone)

        elif choice == "4":
            name = input("Name: ")
            delete_contact(name)

        elif choice == "5":
            key = input("Search: ")
            search_contact(key)

        elif choice == "6":
            insert_from_csv("contacts.csv")

        elif choice == "0":
            break


if __name__ == "__main__":
    menu()