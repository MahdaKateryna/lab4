import psycopg2
import os

DATABASE_URL = os.getenv("postgresql://lab4_2xl1_user:CajMHHbPMlpsRPjYMlM4LsX8nuYksl6X@dpg-d0pkscmmcj7s73e94lug-a/lab4_2xl1")

def get_connection():
    return psycopg2.connect("postgresql://lab4_2xl1_user:CajMHHbPMlpsRPjYMlM4LsX8nuYksl6X@dpg-d0pkscmmcj7s73e94lug-a/lab4_2xl1")

def insert_data(name, email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))

def get_all_data():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name, email FROM users")
            return cur.fetchall()
