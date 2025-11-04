from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return open("index.html").read()

@app.route('/hitung', methods=['POST'])
def hitung():
    data = request.json
    try:
        a = int(data.get("a",0))
        b = int(data.get("b",0))
        hasil = a + b
        return jsonify({"hasil": hasil})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)