import sqlite3

def init_db():
    conn = sqlite3.connect("arinc_429_log.db")
    conn.execute('PRAGMA journal_mode=WAL;')

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arinc_429_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            channel INTEGER,
            raw_message TEXT,
            raw_label TEXT,
            raw_data TEXT,
            raw_ssm TEXT,
            raw_parity TEXT
        )
    ''')

    return conn
