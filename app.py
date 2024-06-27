from flask import Flask, render_template, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption
# You should save this key and keep it safe; it is used for both encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    text = data['text']
    encrypted_text = cipher_suite.encrypt(text.encode()).decode()
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    encrypted_text = data['text']
    try:
        decrypted_text = cipher_suite.decrypt(encrypted_text.encode()).decode()
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
