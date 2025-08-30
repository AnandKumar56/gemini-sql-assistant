import sqlite3
import pandas as pd


import os

def read_sql_query(sql, db_path=None):
    if db_path is None:
        db_path = os.path.join("db", "Naresh_it_employee1.db")
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        col_names = [desc[0] for desc in cur.description]
        conn.close()
        return rows, col_names
    except sqlite3.Error as e:
        return [("SQL Error", str(e))], ["Error"]

def get_db_schema(db_path=None):
    if db_path is None:
        db_path = os.path.join("db", "Naresh_it_employee1.db")
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        schema = {}
        for table in tables:
            tname = table[0]
            cur.execute(f"PRAGMA table_info({tname});")
            columns = cur.fetchall()
            schema[tname] = [(col[1], col[2]) for col in columns]
        conn.close()
        return schema
    except Exception as e:
        return {"Error": str(e)}
