import sqlite3
DATABASE_NAME = "VeriTabani.db"

def GetDB():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def CrateTable(table):
    db = GetDB()
    cursor = db.cursor()
    cursor.execute(table)
