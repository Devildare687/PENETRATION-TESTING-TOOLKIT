from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy credentials for testing
USERNAME = "testuser"
PASSWORD = "securepassword123"

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    
    if username == USERNAME and password == PASSWORD:
        return jsonify({"status": "success", "message": "Login successful!"}), 200
    return jsonify({"status": "fail", "message": "Invalid credentials."}), 401

if __name__ == "__main__":
    app.run(debug=True)
