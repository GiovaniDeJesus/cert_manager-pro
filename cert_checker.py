#!/usr/bin/env python3
from datetime import datetime, UTC
import socket
import ssl

hostname = 'www.example.com'
context = ssl.create_default_context()
with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = ssock.getpeercert()

# Parsing expiration date
not_after = cert["notAfter"]

# Calculate difference from current UTC time
expiry = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
now = datetime.now(UTC)
delta = expiry.replace(tzinfo=UTC) - now
print(delta)
