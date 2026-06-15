import socket
import sys
from datetime import datetime

# 1. Target define karein (Aap domain name ya IP address de sakte hain)
target_input = input("Enter the host to scan (e.g., 127.0.0.1 or google.com): ")

try:
    # Domain name ko IP mein convert karne ke liye
    target_ip = socket.gethostbyname(target_input)
except socket.gaierror:
    print("\n[-] Hostname resolve nahi ho paya. Exiting...")
    sys.exit()

# Scan shuru hone ka time aur details print karein
print("-" * 50)
print(f"Scanning Target: {target_ip}")
print(f"Time Started: {str(datetime.now())}")
print("-" * 50)

# 2. Jin ports ko scan karna hai unki list (Aap ise badal bhi sakte hain)
# Yahan hum kuch common ports scan kar rahe hain
ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 443, 3389]

try:
    for port in ports_to_scan:
        # socket.AF_INET = IPv4, socket.SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 1 second ka timeout set kiya taaki code atak na jaye
        s.settimeout(1.0)
        
        # Connection try karein (connect_ex error code return karta hai, exception nahi fekta)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: CLOSED")
            
        # Socket ko har loop ke baad close karein
        s.close()

except KeyboardInterrupt:
    print("\n[-] Scan ko beech mein hi rok diya gaya (Ctrl+C).")
    sys.exit()

except socket.error:
    print("\n[-] Server se connect nahi ho paa rahe hain.")
    sys.exit()

print("-" * 50)
print("Scan Completed Successfully!")
