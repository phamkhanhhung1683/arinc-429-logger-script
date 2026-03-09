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
            raw_parity_field,
            processed_label_field)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            now,
            message['channel'],
            message['raw_message'],
            message['raw_fields']['label'],
            message['raw_fields']['data'],
            message['raw_fields']['ssm'],
            message['raw_fields']['parity'],
            message['processed_fields']['label']
        ))
        db_conn.commit()

    except Exception as e:
        print(f"[ERROR] Database insertion: {e}")
