from datetime import datetime

from scripts.schemas import ProcessedMessage


def load_message(db_conn, message: ProcessedMessage):
    if not message:
        return

    try:
        cursor = db_conn.cursor()

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        print(now)

        cursor.execute(
            """
            INSERT INTO arinc_429_messages 
            (timestamp,
            string,
            channel,
            raw_message,
            raw_parity,
            raw_data,
            raw_label,
            processed_label,
            message_group,
            message_description,
            processed_data)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                now,
                message["raw_message"]["string"],
                message["raw_message"]["channel"],
                message["raw_message"]["binary"],
                message["raw_message"]["parity"],
                message["raw_message"]["data"],
                message["raw_message"]["label"],
                message["label"],
                message["message_group"],
                message["message_description"],
                message["data"],
            ),
        )
        db_conn.commit()

    except Exception as e:
        print(f"[ERROR] Database insertion: {e}")
