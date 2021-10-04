import database
import functions as f


def insert_game(name, price, rate):
    db = database.GetDB()
    cursor = db.cursor()
    statement = "INSERT INTO games(name, price, rate) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, price, rate])
    db.commit()
    return True


def update_game(id, name, price, rate):
    db = database.GetDB()
    cursor = db.cursor()
    statement = "UPDATE games SET name = ?, price = ?, rate = ? WHERE id = ?"
    cursor.execute(statement, [name, price, rate, id])
    db.commit()
    return True


def delete_game(id):
    db = database.GetDB()
    cursor = db.cursor()
    statement = "DELETE FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = database.GetDB()
    cursor = db.cursor()
    statement = "SELECT id, name, price, rate FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    row_headers = [x[0] for x in cursor.description]
    return f.ResJsonOne(cursor.fetchone(), row_headers)


def get_games():
    db = database.GetDB()
    cursor = db.cursor()
    query = "SELECT id, name, price, rate FROM games"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    return f.ResJson(cursor.fetchall(), row_headers)