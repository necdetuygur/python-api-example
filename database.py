import sqlite3
DATABASE_NAME = "VeriTabani.db"


def GetDB():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def CrateTables():
    tables = [
        """
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                rate INTEGER NOT NULL
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS games2 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                rate INTEGER NOT NULL
            )
        """
    ]
    db = GetDB()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
