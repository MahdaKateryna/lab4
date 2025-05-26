from flask import Flask, request, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return "<h3>Lab 4: Data Storage API</h3>"

@app.route('/add', methods=['POST'])
def add_record():
    data = request.get_json()
    name = data.get('name')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": f"User '{name}' added."}), 201

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
