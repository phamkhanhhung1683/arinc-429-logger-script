import socket
import argparse
import time

def process_arinc(message_string):
    print(f"Processing: {message_string}")

def start_client(host, port):
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
                        print(f"Full message: {line}")
                        print(f"Bytes: {len(line)}")
                        process_arinc(line)

        except Exception as e:
            print(f"Exception: {e}")

        print("Retrying...")
        time.sleep(1)

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
