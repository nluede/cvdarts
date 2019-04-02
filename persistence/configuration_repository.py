import sqlite3

"""
Repository class to persist the configuration of the individual devices
"""


def create_config():
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS configuration (
                    device_id integer PRIMARY KEY,
                    dartboard_level integer NOT NULL
                    )
                    """)

    conn.commit()
    conn.close()


def put_config_for_device(device_id, dartboard_level):
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()

    cursor.execute("INSERT OR REPLACE INTO configuration VALUES (" +
                   str(device_id) +
                   ", " +
                   str(dartboard_level) +
                   ")")

    conn.commit()
    conn.close()


def find_config_for_device(device_id):
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM configuration WHERE device_id=" + str(device_id))
    result = cursor.fetchone()

    conn.commit()
    conn.close()

    return result
