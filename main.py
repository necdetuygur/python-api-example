from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

import _Kisi

@app.route('/', methods=["GET"])
def Base():
    return """
        <div><a href="Kisi.html">Kisi</a></div>
    """

@app.route('/<path:path>')
def send_public(path):
    return send_from_directory('public', path)

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8070, debug=True)
