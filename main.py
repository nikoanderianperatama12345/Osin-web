from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return open("index.html").read()  # Tampilkan frontend

@app.route('/run', methods=['POST'])
def run_osin():
    data = request.json
    target = data.get('target')

    if not target:
        return jsonify({"error":"Target kosong"}), 400

    try:
        # Jalankan Osin asli
        result = subprocess.getoutput(f'python3 osin.py {target}')
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)