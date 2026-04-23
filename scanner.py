import socket

target = input("Enter target IP or domain: ")

# Convert domain to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid target")
    exit()

print(f"\nScanning target: {target_ip}\n")

# Common ports list
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is CLOSED")

    sock.close()
    
