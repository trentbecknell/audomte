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
    cur.execute('''
    CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT,
        default_price REAL NOT NULL,
        is_active INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS deliveries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        project_id INTEGER,
        service_id INTEGER NOT NULL,
        filename TEXT NOT NULL,
        file_path TEXT NOT NULL,
        file_size INTEGER,
        price REAL NOT NULL,
        download_token TEXT NOT NULL UNIQUE,
        token_expires_at TIMESTAMP,
        download_count INTEGER DEFAULT 0,
        max_downloads INTEGER DEFAULT 3,
        status TEXT DEFAULT 'pending',  -- pending | notified | downloaded | paid | expired
        payment_method TEXT,  -- zelle | paypal | cashapp | venmo | other
        payment_confirmed INTEGER DEFAULT 0,
        payment_confirmed_at TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        notified_at TIMESTAMP,
        FOREIGN KEY(client_id) REFERENCES clients(id),
        FOREIGN KEY(project_id) REFERENCES projects(id),
        FOREIGN KEY(service_id) REFERENCES services(id)
    );''')
    
    # Insert default services if they don't exist
    cur.execute('''
    INSERT OR IGNORE INTO services (name, description, default_price) VALUES
        ('Mixing', 'Professional stereo mix', 150.00),
        ('Mastering', 'Professional mastering', 100.00),
        ('Production', 'Full production service', 500.00),
        ('Stem Mix', 'Stems mixing service', 200.00),
        ('Revisions', 'Mix/master revisions', 50.00),
        ('Custom', 'Custom service - price on quote', 0.00)
    ''')
    
    conn.commit()
    conn.close()
