from flask import Flask, request, jsonify
from db import get_connection, create_table
import os
import traceback

app = Flask(__name__)

# Головна сторінка
@app.route("/")
def index():
    return "✅ Lab 4 is running with PostgreSQL!"

# Роут для ініціалізації бази (створення таблиці)
@app.route("/init")
def init_db():
    try:
        create_table()
        return "✅ Table 'users' created or already exists!"
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# Роут для додавання користувача
@app.route("/add", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
        if not data or "name" not in data or "email" not in data:
            return jsonify({"error": "Missing 'name' or 'email' in request"}), 400

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)",
                    (data["name"], data["email"]))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success"}), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# Роут для отримання всіх користувачів
@app.route("/users", methods=["GET"])
def get_users():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# Роут для дебагу змінної середовища (перевірити чи підставляється DATABASE_URL)
@app.route("/debug")
def debug():
    return jsonify({"DATABASE_URL": os.getenv("DATABASE_URL")})
