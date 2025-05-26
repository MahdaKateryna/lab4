import psycopg2
import os

DATABASE_URL = os.getenv("postgresql://lab4_2xl1_user:CajMHHbPMlpsRPjYMlM4LsX8nuYksl6X@dpg-d0pkscmmcj7s73e94lug-a.oregon-postgres.render.com/lab4_2xl1")  # Render provides this automatically

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def create_users_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                );
            """)

def insert_user(name, email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))