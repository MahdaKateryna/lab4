import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def insert_data(name, email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))

def get_all_data():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name, email FROM users")
            return cur.fetchall()
