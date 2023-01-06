#!/usr/bin/python3
# Para ejecutar este script y obtener los puertos: python3 ports.py 2>&1 | grep "[+]" | awk '{print $8}' | tr -d ':'
from pwn import *
import socket

server = input("[+] Introduce la maquina victima a enumerar: ")

for port in range(1, 65535):
    try:
        conn = remote(server, port)

        print("Puerto", port)

        conn.close()
    except:
        pass

