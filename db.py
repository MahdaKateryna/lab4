import psycopg2
import os

def get_db_connection():
    return psycopg2.connect(
        url=os.getenv("postgresql://lab4_2xl1_user:CajMHHbPMlpsRPjYMlM4LsX8nuYksl6X@dpg-d0pkscmmcj7s73e94lug-a/lab4_2xl1"),
        dbname=os.getenv("lab4_2xl1"),
        user=os.getenv("lab4_2xl1_user"),
        password=os.getenv("CajMHHbPMlpsRPjYMlM4LsX8nuYksl6X"),
        host=os.getenv("dpg-d0pkscmmcj7s73e94lug-a"),
        port=os.getenv("5432")
    )
