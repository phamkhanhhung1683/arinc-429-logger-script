import socket
import argparse
import time
import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect("arinc_429_log.db")
    conn.execute('PRAGMA journal_mode=WAL;')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arinc_429_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            label TEXT,
            sdi TEXT,
            data TEXT,
            ssm TEXT,
            parity TEXT,
            channel INTEGER,
            binary TEXT
        )
    ''')

    return conn


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
        data   = final_bits[3:22]
        sdi    = final_bits[22:24]
        label  = final_bits[24:32]

        result = {
            "channel": channel,
            "binary": final_bits,
            "fields": {
                "parity": parity,
                "ssm": ssm,
                "data": data,
                "sdi": sdi,
                "label": label
            }
        }
        print(result)

        return result

    except Exception as e:
        print(f"Decoding error: {e}")
        return None


def save_to_db(conn, data):
    if not data:
        return

    try:
        cursor = conn.cursor()
        fields = data['fields']

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print(now)

        cursor.execute('''
            INSERT INTO arinc_429_messages 
            (timestamp, label, sdi, data, ssm, parity, channel, binary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            now,
            fields['label'],
            fields['sdi'],
            fields['data'],
            fields['ssm'],
            fields['parity'],
            data['channel'],
            data['binary']
        ))
        conn.commit()
    except Exception as e:
        print(f"Database insertion error: {e}")


def start_client(host, port):
    db_conn = init_db()
    try:
        while True:
            buffer = ""
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    print(f"Connecting to the ARINC 429 LAN board at {host}:{port}...")
                    client_socket.connect((host, port))
                    print(f"Connected to the ARINC 429 LAN board at {host}:{port}")

                    while True:
                        data = client_socket.recv(4096)

                        if not data:
                            print("Connection closed")
                            break

                        buffer += data.decode('ascii', errors='ignore')
                        lines = buffer.split('\n')
                        buffer = lines.pop()

                        for line in lines:
                            print(f"Line: {line}")
                            print(f"Length: {len(line)}")
                            result = decode_arinc_429_word(line)
                            if result:
                                save_to_db(db_conn, result)
                            print()

            except Exception as e:
                print(f"Network error: {e}")

            print("Retrying...")
            time.sleep(1)
    finally:
        db_conn.close()
        print("Database connection closed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP client receiving data from an ARINC 429 LAN board")
    
    parser.add_argument(
        "--host", 
        type=str, 
        default="192.168.24.190", 
        help="Board IP address (default: 192.168.24.190)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=10001, 
        help="Board port number (default: 10001)"
    )

    args = parser.parse_args()

    start_client(args.host, args.port)
