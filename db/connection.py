import sqlite3

def get_connection(db_path="netscope.db"):
    return sqlite3.connect(db_path)
