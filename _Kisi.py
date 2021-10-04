from __main__ import app
from flask import Flask, jsonify, request
import database
import functions as f

database.CrateTable("""
    CREATE TABLE IF NOT EXISTS Kisi (
        KisiID INTEGER PRIMARY KEY AUTOINCREMENT,
        TcKimlikNo TEXT NOT NULL,
        Ad TEXT NOT NULL,
        Soyad TEXT NOT NULL,
        DogumYeri TEXT NOT NULL,
        DogumTarihi TEXT NOT NULL,
        IkametgahAdresi TEXT NOT NULL
    )
""")

@app.route('/Kisi', methods=["GET"])
def KisiGetAll():
    db = database.GetDB()
    cursor = db.cursor()
    query = "SELECT KisiID, TcKimlikNo, Ad, Soyad, DogumYeri, DogumTarihi, IkametgahAdresi FROM Kisi"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    return f.ResJson(cursor.fetchall(), row_headers)


@app.route("/Kisi/<id>", methods=["GET"])
def KisiGetById(id):
    db = database.GetDB()
    cursor = db.cursor()
    statement = "SELECT KisiID, TcKimlikNo, Ad, Soyad, DogumYeri, DogumTarihi, IkametgahAdresi FROM Kisi WHERE KisiID = ?"
    cursor.execute(statement, [id])
    row_headers = [x[0] for x in cursor.description]
    return f.ResJsonOne(cursor.fetchone(), row_headers)


@app.route("/Kisi", methods=["POST"])
def KisiAdd():
    details = request.get_json()

    TcKimlikNo = details["TcKimlikNo"]
    Ad = details["Ad"]
    Soyad = details["Soyad"]
    DogumYeri = details["DogumYeri"]
    DogumTarihi = details["DogumTarihi"]
    IkametgahAdresi = details["IkametgahAdresi"]

    db = database.GetDB()
    cursor = db.cursor()
    statement = "INSERT INTO Kisi(TcKimlikNo, Ad, Soyad, DogumYeri, DogumTarihi, IkametgahAdresi) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [TcKimlikNo, Ad, Soyad,
                   DogumYeri, DogumTarihi, IkametgahAdresi])
    db.commit()
    return jsonify(True)


@app.route("/Kisi", methods=["PUT"])
def KisiSet():
    details = request.get_json()

    KisiID = details["KisiID"]
    TcKimlikNo = details["TcKimlikNo"]
    Ad = details["Ad"]
    Soyad = details["Soyad"]
    DogumYeri = details["DogumYeri"]
    DogumTarihi = details["DogumTarihi"]
    IkametgahAdresi = details["IkametgahAdresi"]

    db = database.GetDB()
    cursor = db.cursor()
    statement = "UPDATE Kisi SET TcKimlikNo = ?, Ad = ?, Soyad = ?, DogumYeri = ?, DogumTarihi = ?, IkametgahAdresi = ? WHERE KisiID = ?"
    cursor.execute(statement, [TcKimlikNo, Ad, Soyad,
                   DogumYeri, DogumTarihi, IkametgahAdresi, KisiID])
    db.commit()
    return jsonify(True)


@app.route("/Kisi/<id>", methods=["DELETE"])
def KisiDelete(id):
    db = database.GetDB()
    cursor = db.cursor()
    statement = "DELETE FROM Kisi WHERE KisiID = ?"
    cursor.execute(statement, [id])
    db.commit()
    return jsonify(True)
