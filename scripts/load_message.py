from datetime import datetime


def load_message(db_conn, message):
    if not message:
        return

    try:
        cursor = db_conn.cursor()

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print(now)

        cursor.execute('''
            INSERT INTO arinc_429_messages 
            (timestamp,
            channel,
            raw_message,
            raw_label_field,
            raw_data_field,
            raw_ssm_field,
            raw_parity_field)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            now,
            message['channel'],
            message['binary'],
            message['fields']['label'],
            message['fields']['data'],
            message['fields']['ssm'],
            message['fields']['parity'],
        ))
        db_conn.commit()

    except Exception as e:
        print(f"[ERROR] Database insertion: {e}")
