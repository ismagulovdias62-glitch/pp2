import psycopg2
from connect import connect


def call_upsert(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()


def search_pattern(pattern):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
    print(cur.fetchall())

    cur.close()
    conn.close()


def paginate(limit, offset):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)",
                (limit, offset))
    print(cur.fetchall())

    cur.close()
    conn.close()


def delete_value(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (value,))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    call_upsert("Alice", "123456")
    search_pattern("Ali")
    paginate(5, 0)
    delete_value("Alice")