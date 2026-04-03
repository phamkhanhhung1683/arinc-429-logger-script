import sqlite3

from scripts.schemas import ProcessedMessage

conn = sqlite3.connect("arinc_429_messages.db")
conn.execute("PRAGMA journal_mode=WAL;")

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS arinc_429_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME,
        raw_string TEXT,
        channel INTEGER,
        raw_message TEXT,
        raw_parity TEXT,
        raw_data TEXT,
        raw_label TEXT,
        parity_ok BOOLEAN,
        processed_label TEXT,
        message_group TEXT,
        message_description TEXT,
        processed_data TEXT
    )
""")


def load_message(message: ProcessedMessage):
    if not message:
        return

    try:
        cursor.execute(
            """
            INSERT INTO arinc_429_messages 
            (timestamp,
            raw_string,
            channel,
            raw_message,
            raw_parity,
            raw_data,
            raw_label,
            parity_ok,
            processed_label,
            message_group,
            message_description,
            processed_data)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                message["raw_message"]["timestamp"],
                message["raw_message"]["string"],
                message["raw_message"]["channel"],
                message["raw_message"]["binary"],
                message["raw_message"]["parity"],
                message["raw_message"]["data"],
                message["raw_message"]["label"],
                message["parity_ok"],
                message["label"],
                message["message_group"],
                message["message_description"],
                message["data"],
            ),
        )
        conn.commit()

    except Exception as e:
        print(f"[ERROR] Database insertion: {e}")
