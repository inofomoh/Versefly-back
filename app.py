from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.film_generator import generate_film

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return '🎬 Versefly backend is running!'

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    title = data.get('title', 'Untitled Film')
    script = data.get('script', '')

    try:
        output_path = generate_film(title, script)
        return jsonify({"status": "success", "film": output_path})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})