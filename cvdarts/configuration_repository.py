import sqlite3


def create():
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS configuration (
                    device_id integer NOT NULL,
                    dartboard_level integer NOT NULL
                    )
                    """)

    conn.commit()
    conn.close()


def insert(device_id, dartboard_level):
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO configuration VALUES (" +
                   str(device_id) +
                   ", " +
                   str(dartboard_level) +
                   ")")

    conn.commit()
    conn.close()


def findAll():
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM configuration")
    result = cursor.fetchall()

    conn.commit()
    conn.close()

    return result