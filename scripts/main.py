import argparse
import socket
import time

from init_db import init_db
from extract_and_load_raw_message import extract_and_load_raw_message


def start_client(host, port):
    db_conn = init_db()
    try:
        while True:
            buffer = ""
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    print(f"[INFO] Connecting to the ARINC 429 LAN board at {host}:{port}...")
                    client_socket.settimeout(5)
                    client_socket.connect((host, port))
                    print(f"[INFO] Connected to the ARINC 429 LAN board at {host}:{port}")

                    while True:
                        data = client_socket.recv(4096)

                        if not data:
                            print("[INFO] Connection closed")
                            break

                        buffer += data.decode('ascii', errors='ignore')
                        lines = buffer.split('\n')
                        buffer = lines.pop()

                        for line in lines:
                            print(f"Line: {line}")
                            print(f"Length: {len(line)}")

                            extract_and_load_raw_message(db_conn, line)

                            print()

            except Exception as e:
                print(f"[ERROR] Network: {e}")

            print("[INFO] Reconnecting...")
            time.sleep(1)
    finally:
        db_conn.close()
        print("[INFO] Database connection closed")


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
