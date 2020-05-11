import sqlite3


def get_connection():
    return sqlite3.connect('ship_configurations.db')  # this even creates the file if it doesn't exist
