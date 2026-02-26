# Script for the TCP client receiving data from an ARINC 429 LAN board

## Usage

```sh
python3 main.py [-h] [--host HOST] [--port PORT]

options:
  -h, --help   show this help message and exit
  --host HOST  Board IP address (default: 192.168.24.190)
  --port PORT  Board port number (default: 10001)
```

## Example

```sh
python3 main.py --host 192.168.24.190 --port 10001
```
