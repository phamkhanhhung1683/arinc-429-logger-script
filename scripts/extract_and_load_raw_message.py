from datetime import datetime


def decode_arinc_429_word(raw_str):
    if not raw_str or len(raw_str) != 9:
        return None

    try:
        first_char = raw_str[0]
        if not first_char.isupper():
            return None
        channel = ord(first_char) - 64

        payload = raw_str[1:]
        reversed_payload = payload[::-1]

        binary_str = ""
        for char in reversed_payload:
            val = ord(char) - 97
            if 0 <= val <= 15:
                binary_str += format(val, '04b')
            else:
                return None

        final_bits = binary_str[::-1]

        parity = final_bits[0]
        ssm    = final_bits[1:3]
        data   = final_bits[3:24]
        label  = final_bits[24:32]

        result = {
            "channel": channel,
            "binary": final_bits,
            "fields": {
                "parity": parity,
                "ssm": ssm,
                "data": data,
                "label": label
            }
        }
        print(result)
        return result

    except Exception as e:
        print(f"[ERROR] Decoding: {e}")
        return None


def load_raw_message(db_conn, raw_message):
    if not raw_message:
        return

    try:
        cursor = db_conn.cursor()

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print(now)

        cursor.execute('''
            INSERT INTO arinc_429_messages 
            (timestamp, channel, raw_message, raw_label, raw_data, raw_ssm, raw_parity)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            now,
            raw_message['channel'],
            raw_message['binary'],
            raw_message['fields']['label'],
            raw_message['fields']['data'],
            raw_message['fields']['ssm'],
            raw_message['fields']['parity'],
        ))
        db_conn.commit()

    except Exception as e:
        print(f"[ERROR] Database insertion: {e}")


def extract_and_load_raw_message(db_conn, raw_str):
    result = decode_arinc_429_word(raw_str)
    if result:
        load_raw_message(db_conn, result)
