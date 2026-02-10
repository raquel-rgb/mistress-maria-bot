import sqlite3
import os

DB_PATH = 'data/users.db'

def init_db():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total_tributes REAL DEFAULT 0,
            last_task_date TEXT,
            punishment_count INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()

def add_user(user_id, username, first_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR IGNORE INTO users (user_id, username, first_name)
        VALUES (?, ?, ?)
    ''', (user_id, username, first_name))
    
    conn.commit()
    conn.close()

def update_tribute(user_id, amount):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE users SET total_tributes = total_tributes + ?
        WHERE user_id = ?
    ''', (amount, user_id))
    
    conn.commit()
    conn.close()

def increment_punishment(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE users SET punishment_count = punishment_count + 1
        WHERE user_id = ?
    ''', (user_id,))
    
    conn.commit()
    conn.close()

# Initialize database on import
init_db()
