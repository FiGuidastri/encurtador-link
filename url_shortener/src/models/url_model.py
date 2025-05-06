import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'urls.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('CREATE TABLE IF NOT EXISTS urls (id TEXT PRIMARY KEY, original_url TEXT)')
    conn.close()

def save_url(short_id, original_url):
    conn = sqlite3.connect(DB_PATH)
    conn.execute('INSERT INTO urls (id, original_url) VALUES (?, ?)', (short_id, original_url))
    conn.commit()
    conn.close()

def get_original_url(short_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.execute('SELECT original_url FROM urls WHERE id = ?', (short_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None