from flask import Flask, request, jsonify
from morse_converter import tamil_to_morse_code, morse_code_to_tamil

app = Flask(__name__)

@app.route('/tamil_to_morse', methods=['POST'])
def tamil_to_morse_endpoint():
    data = request.json
    tamil_text = data.get('tamil_text', '')
    morse_code = tamil_to_morse_code(tamil_text)
    return jsonify({'morse_code': morse_code})

@app.route('/morse_to_tamil', methods=['POST'])
def morse_to_tamil_endpoint():
    data = request.json
    morse_code = data.get('morse_code', '')
    tamil_text = morse_code_to_tamil(morse_code)
    return jsonify({'tamil_text': tamil_text})

if __name__ == '__main__':
    app.run(debug=True)
