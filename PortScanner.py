#!/bin/python3

import sys
import socket
from datetime import datetime

# Defining our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
else:
    print("Invalid number of arguments")
    print("Syntax: python3 PortScanner.py <valid_ip_address>")
    sys.exit()

print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)
        result = s.connect_ex((target, port))
        if result == 0:
            service_name = socket.getservbyport(port)  # Get service name
            print(f"Port {port} ({service_name}) is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Could not connect to the server")
    sys.exit()
