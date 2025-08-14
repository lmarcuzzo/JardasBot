import sqlite3
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE = os.getenv("DATABASE")

##############################################################################
def db_select_one(query: str, params: tuple = ()):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        with conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        if conn is not None:
            conn.close()


def db_select_all(query: str, params: tuple = ()):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        with conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        if conn is not None:
            conn.close()


def db_execute_query(query: str, params: tuple = ()):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        with conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        if conn is not None:
            conn.close()
