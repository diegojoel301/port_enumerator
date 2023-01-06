#!/usr/bin/python3
# Para ejecutar este script y obtener los puertos: python3 ports.py 2>&1 | grep "[+]" | awk '{print $8}' | tr -d ':'
from pwn import *
import socket
import sys

try:
    server = sys.argv[1]    
except:
    print("Error no especificaste la direccion IP")
    print("[+] Forma correcta de ejecutar el script:")
    print("\tpython3 ports.py <ip> 2>&1 | grep \"[+]\" | awk '{print $8}' | tr -d ':'")
    sys.exit(1)

for port in range(1, 65535):
    try:
        conn = remote(server, port)

        print("Puerto", port)

        conn.close()
    except:
        pass

