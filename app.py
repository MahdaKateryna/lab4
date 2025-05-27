from flask import Flask, request, jsonify
from db import get_connection, create_table

app = Flask(__name__)
create_table()


@app.route("/")
def index():
    return "Lab 4 is running with PostgreSQL!"


@app.route("/add", methods=["POST"])
def add_user():
    data = request.get_json()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)",
                (data["name"], data["email"]))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "success"}), 201


@app.route("/users", methods=["GET"])
def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)
