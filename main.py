from flask import Flask, jsonify, request

app = Flask(__name__)

import _Kisi

@app.route('/', methods=["GET"])
def Base():
    return """
        /Kisi
    """

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8070, debug=True)
