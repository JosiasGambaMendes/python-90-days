server_num = int(input("Enter the number of servers you want to register: "))

print("\n=== Server Inventory Builder ===\n")

for i in range(1, server_num + 1):
    hostname = input(f"Enter hostname for server {i}: ")
    ip = input(f"Enter IP for server {i}: ")

    print(f"\nServer {i}")
    print(f"Hostname: {hostname}")
    print(f"IP: {ip}")
    print("-" * 30)