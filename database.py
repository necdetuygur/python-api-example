import sqlite3
DATABASE_NAME = "VeriTabani.db"


def GetDB():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def CrateTables():
    tables = [
        """
            CREATE TABLE IF NOT EXISTS Kisi (
                KisiID INTEGER PRIMARY KEY AUTOINCREMENT,
                TcKimlikNo TEXT NOT NULL,
                Ad TEXT NOT NULL,
                Soyad TEXT NOT NULL,
                DogumYeri TEXT NOT NULL,
                DogumTarihi TEXT NOT NULL,
                IkametgahAdresi TEXT NOT NULL
            )
        """
    ]
    db = GetDB()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
