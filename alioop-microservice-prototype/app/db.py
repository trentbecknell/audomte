import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "alioop.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        delivery_pref TEXT DEFAULT 'Drive',
        delivery_custom_url TEXT,
        payment_pref TEXT DEFAULT 'Stripe',
        payment_custom_url TEXT,
        use_masked_phone INTEGER DEFAULT 0
    );''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        status TEXT DEFAULT 'active',
        notes TEXT,
        FOREIGN KEY(client_id) REFERENCES clients(id)
    );''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS masked_phones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL UNIQUE,
        real_phone TEXT NOT NULL,
        masked_phone TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(client_id) REFERENCES clients(id)
    );''')
    conn.commit()
    conn.close()
