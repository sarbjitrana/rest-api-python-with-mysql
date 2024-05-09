from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import mysql.connector
from dotenv import load_dotenv
import os
from PIL import Image
import pytesseract

# Load environment variables from .env file
load_dotenv()

# Access environment variables
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

app = Flask(__name__)
bcrypt = Bcrypt()

# Connect to MySQL
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = db.cursor()

# User Signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user and bcrypt.check_password_hash(user[2], password):
        return jsonify({'message': 'Login successful', 'access_token': 'some_access_token'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

# User Logout
@app.route('/logout', methods=['POST'])
def logout():
    # Here you can handle invalidating access tokens
    return jsonify({'message': 'Logged out successfully'}), 200

# Password Reset
@app.route('/password-reset', methods=['POST'])
def password_reset():
    # Implement password reset logic here
    return jsonify({'message': 'Password reset successfully'}), 200

# Token Refresh
@app.route('/token-refresh', methods=['POST'])
def token_refresh():
    # Implement token refresh logic here
    return jsonify({'message': 'Token refreshed successfully'}), 200

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img = Image.open(image_file)
        text = pytesseract.image_to_string(img)
        return jsonify({'text': text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
