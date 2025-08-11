from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint 1: /check
@app.route('/check', methods=['GET'])
def check():
    return "OK", 200

# Endpoint 2: /info
@app.route('/info', methods=['GET'])
def info():
    data = {
        "Instancia": "Maquina 1 - Api 1",
        "Curso": "Seminario De Sistemas 1 A",
        "Grupo": "Grupo 7"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
